from django.views.generic import DetailView, ListView, CreateView, UpdateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
from django.shortcuts import redirect
from django.db.models import Count, Q
from django.db import transaction
from django.conf import settings

from gallery.models import Group, GroupMembership, GalleryProfile
from gallery.forms import CreateGroupForm

import logging
logger = logging.getLogger(__name__)

class GroupDetail(DetailView):
    model = Group

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        prefs = GalleryProfile.get_prefs(self.request.user)

        submissions = ctx['object'].submission_set.filter(is_visible=True)
        if not prefs['show_nsfw']:
            submissions = submissions.filter(is_nsfw=False)
        
        paginator = Paginator(submissions, 10)
        user = self.request.user
        if user.is_authenticated:
            try:
                my_membership = self.object.groupmembership_set.get(user=user).status
            except GroupMembership.DoesNotExist:
                my_membership = None
        else:
            my_membership = None
            
        if my_membership == GroupMembership.STATUS_MOD:
            pending = self.object.groupmembership_set.filter(status=GroupMembership.STATUS_PENDING).count()
            banned = self.object.groupmembership_set.filter(status=GroupMembership.STATUS_BANNED)

        else:
            pending = 0
            banned = None

        return {**ctx,
            'paginator': paginator,
            'page_obj': paginator.page(self.request.GET.get('page', 1)),
            'members': ctx['object'].groupmembership_set.filter(status__in=GroupMembership.MEMBER_STATUSES).order_by('-status', 'user__username'),
            'my_membership': my_membership,
            'pending_members': pending,
            'banned_members': banned,
        }

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if request.user.is_authenticated:
            if request.POST['action'] == 'join' and not self.object.groupmembership_set.filter(user=request.user).exists():
                GroupMembership.objects.create(
                    group=self.object,
                    user=request.user,
                    status=GroupMembership.STATUS_PENDING if self.object.approve_joins else GroupMembership.STATUS_MEMBER
                )

        return redirect(self.object)


class GroupList(ListView):
    model = Group

    def get_queryset(self):
        return self.model.objects.annotate(
            member_count=Count('users'),
            submission_count=Count('submission'),
        ).order_by('title')


class GroupPending(DetailView):
    model = Group
    template_name_suffix = '_pending'

    def get_context_data(self, **kwargs):
        if not self.object.can_edit(self.request.user):
            raise Http404

        ctx = super().get_context_data(**kwargs)
        
        applicants = []
        
        prefs = GalleryProfile.get_prefs(self.request.user)
        q = Q(is_visible=True)
        if not prefs['show_nsfw']:
            q &= Q(is_nsfw=False)

        for user in self.object.users.filter(groupmembership__status=GroupMembership.STATUS_PENDING):
            applicants.append({
                'user': user,
                'submissions': user.submission_set.filter(q)[:3]
            })
        
        return {
            **ctx,
            'applicants': applicants,
        }
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if not self.object.can_edit(self.request.user):
            raise Http404
        
        if request.POST['action'] == 'induct':
            GroupMembership.objects.filter(group=self.object, user_id=request.POST['user'], status=GroupMembership.STATUS_PENDING).update(status=GroupMembership.STATUS_MEMBER)
        elif request.POST['action'] == 'reject':
            GroupMembership.objects.filter(group=self.object, user_id=request.POST['user'], status=GroupMembership.STATUS_PENDING).delete()
        elif request.POST['action'] == 'ban':
            GroupMembership.objects.filter(group=self.object, user_id=request.POST['user'], status=GroupMembership.STATUS_PENDING).update(status=GroupMembership.STATUS_BANNED)
        
        if GroupMembership.objects.filter(group=self.object, status=GroupMembership.STATUS_PENDING).exists():
            return redirect('gallery:group-pending', slug=self.object.slug)
        else:
            return redirect(self.object)


@method_decorator(login_required, name='dispatch')
class CreateGroup(CreateView):
    form_class = CreateGroupForm
    template_name_suffix = '_create'
    model = Group

    def form_valid(self, form):
        with transaction.atomic():
            group = form.save()
            GroupMembership.objects.create(
                group=group,
                user=self.request.user,
                status=GroupMembership.STATUS_MOD
            )

        logger.info("Group #%d (%s) created by user #%d (%s)",
            group.id,
            group.title,
            self.request.user.id,
            self.request.user.username
        )

        return redirect(group)
    

@method_decorator(login_required, name='dispatch')
class EditGroup(UpdateView):
    model = Group
    fields = ('logo', 'description', 'server_address', 'website', 'approve_joins')

    def get_object(self):
        obj = super().get_object()
        if not obj.can_edit(self.request.user):
            raise Http404
        return obj
    
    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        return {
            **ctx,
            'extauthkey': settings.DRAWPILE_EXT_AUTH['PUBLIC_KEY']
        }


@method_decorator(login_required, name='dispatch')
class LeaveGroup(DetailView):
    model = Group
    template_name = 'gallery/group_leave.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        
        return {**ctx,
            'is_moderator': ctx['object'].groupmembership_set.filter(user=self.request.user, status=GroupMembership.STATUS_MOD).exists(),
            'mods': ctx['object'].groupmembership_set.filter(status=GroupMembership.STATUS_MOD).exclude(user=self.request.user).select_related('user'),
            'members': ctx['object'].groupmembership_set.filter(status=GroupMembership.STATUS_MEMBER).exclude(user=self.request.user).select_related('user').order_by('user__username'),
            'is_last': ctx['object'].groupmembership_set.filter(status__in=GroupMembership.MEMBER_STATUSES).count() == 1,
        }
    
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)

        with transaction.atomic():
            if context['is_moderator'] and not context['is_last'] and not context['mods']:
                successors = request.POST.getlist('user')
                
                if not successors:
                    return self.render_to_response(context)
            
                self.object.groupmembership_set.filter(user_id__in=successors).update(status=GroupMembership.STATUS_MOD)

            self.object.groupmembership_set.filter(user=request.user).delete()

            if context['is_last']:
                return redirect('/gallery/')
        
            else:
                return redirect(self.object)
