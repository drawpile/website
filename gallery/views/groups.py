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

        ctx.update({
            'paginator': paginator,
            'page_obj': paginator.page(self.request.GET.get('page', 1)),
            'members': ctx['object'].groupmembership_set.filter(status__in=GroupMembership.MEMBER_STATUSES).order_by('-status', 'user__username'),
            'my_membership': my_membership,
            'pending_members': pending,
            'banned_members': banned,
        })
        return ctx


class GroupList(ListView):
    model = Group

    def get_queryset(self):
        return self.model.objects.annotate(
            member_count=Count('users'),
            submission_count=Count('submission'),
        ).order_by('title')


@method_decorator(login_required, name='dispatch')
class LeaveGroup(DetailView):
    model = Group
    template_name = 'gallery/group_leave.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        
        ctx.update({
            'is_moderator': ctx['object'].groupmembership_set.filter(user=self.request.user, status=GroupMembership.STATUS_MOD).exists(),
            'mods': ctx['object'].groupmembership_set.filter(status=GroupMembership.STATUS_MOD).exclude(user=self.request.user).select_related('user'),
            'members': ctx['object'].groupmembership_set.filter(status=GroupMembership.STATUS_MEMBER).exclude(user=self.request.user).select_related('user').order_by('user__username'),
            'is_last': ctx['object'].groupmembership_set.filter(status__in=GroupMembership.MEMBER_STATUSES).count() == 1,
        })
        return ctx
    
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
