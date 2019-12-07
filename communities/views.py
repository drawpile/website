from django.views.generic import (
    TemplateView, CreateView, ListView, DetailView, UpdateView
)
from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import transaction
from django.http import Http404
from django.conf import settings

from dpauth.settings import extauth_settings
from .models import Community, Membership
from .forms import EditCommunityForm, ReviewForm
from .webhooks import send_review_notification
from .api.querysets import get_community_list_queryset


class FrontPage(ListView):
    def get_queryset(self):
        qs = get_community_list_queryset(self.request.user)\
            .order_by('-status', 'title')\
            .only('slug', 'badge', 'title', 'short_description')

        user = self.request.user
        if 'mine' in self.request.GET and user.is_authenticated:
            qs = qs.filter(users=user)

        return qs


class YchPage(TemplateView):
    template_name = 'communities/ych.html'


class GuideLinesPage(TemplateView):
    template_name = 'communities/ccg.html'


class SubmitPage(LoginRequiredMixin, CreateView):
    template_name = 'communities/edit.html'
    form_class = EditCommunityForm

    def form_valid(self, form):
        with transaction.atomic():
            self.object = form.save()
            Membership.objects.create(
                user=self.request.user,
                community=self.object,
                status=Membership.STATUS_ADMIN
            )

        notification_url = getattr(settings, 'ADMIN_REPORT_WEBHOOK', '')
        if notification_url:
            send_review_notification(
                notification_url,
                self.object,
                self.request.user
            )

        return redirect(self.object)


class EditPage(LoginRequiredMixin, UpdateView):
    template_name = 'communities/edit.html'
    form_class = EditCommunityForm
    queryset = Community.objects.all()

    def get_object(self):
        obj = super().get_object()
        if not obj.can_admin(self.request.user):
            raise Http404
        return obj


class CommunityPage(DetailView):
    template_name = 'communities/community.html'

    def get_template_names(self):
        obj = self.get_object()
        if (
            obj.content_rating == Community.CONTENT_ADULT and
            obj.my_membership is None and
            not self.request.session.get('am_adult', False)
        ):
            return ['communities/age_gate.html']

        return [self.template_name]

    def get_object(self):
        if not hasattr(self, '_object'):
            qs = get_community_list_queryset(self.request.user)

            try:
                self._object = qs.get(slug=self.kwargs[self.slug_url_kwarg])
                self._object.my_membership = None
                if self.request.user.is_authenticated:
                    try:
                        self._object.my_membership = Membership.objects.get(
                            community=self._object,
                            user=self.request.user
                        )
                    except Membership.DoesNotExist:
                        pass

            except Community.DoesNotExist:
                raise Http404

        return self._object

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        obj = ctx['object']

        ctx['membership'] = obj.my_membership

        if (
            obj.status == Community.STATUS_SUBMITTED
            and self.request.user.has_perm('communities.change_community')
        ):
            ctx['review_form'] = ReviewForm(initial={
                'comment': obj.review_message
            })
        
        if (
            getattr(settings, 'COMMUNITY_ABUSE_REPORT_WEBHOOK', '') and
            self.request.user.is_authenticated
        ):
            ctx['can_report'] = True

        return ctx


def community_confirm_age(request, slug):
    if request.method == 'POST':
        request.session['am_adult'] = True
    return redirect('communities:community', slug=slug)


class ServerHelpPage(DetailView):
    template_name = 'communities/server-help.html'

    def get_object(self):
        qs = get_community_list_queryset(self.request.user)

        try:
            obj = qs.get(slug=self.kwargs[self.slug_url_kwarg])
        except Community.DoesNotExist:
            raise Http404
        
        if not obj.can_admin(self.request.user):
            raise Http404
        
        return obj

    def get_context_data(self, **kwargs):
        return super().get_context_data(
            public_key=extauth_settings['PUBLIC_KEY'],
            **kwargs
        )


class Memberlist(DetailView):
    template_name = 'communities/memberlist.html'
    queryset = Community.objects.all()

    def get_object(self):
        community = super().get_object()
        if not community.can_see_memberlist(self.request.user):
            raise Http404
        return community


def review_community(request, slug):
    if not request.user.has_perm('communities.change_community'):
        raise Http404

    community = get_object_or_404(Community, slug=slug)

    if (
        request.method == 'POST' and
        community.status == Community.STATUS_SUBMITTED
    ):
        form = ReviewForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data

            community.status = cd['verdict']
            community.review_message = cd['comment']
            community.save(update_fields=('status', 'review_message'))

    return redirect(community)
