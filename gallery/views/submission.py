from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View, DetailView, FormView, UpdateView
from django.shortcuts import redirect, get_object_or_404, render
from django.db.models import Q
from django.http import HttpResponse, Http404
from django.utils import timezone
from django.db import transaction
from django.conf import settings

from gallery.models import Group, Submission, Picture, Favorited, Comment
from gallery.forms import ContentSubmissionForm, EditSubmissionForm
from gallery import pictures

class ViewSubmission(DetailView):
    template_name = 'gallery/view_submission.html'
    
    def get_queryset(self):
        filter = Q(is_visible=True)
        if self.request.user.is_authenticated:
            filter |= Q(uploaded_by=self.request.user)
        return Submission.objects.filter(filter)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)

        if self.request.user.is_authenticated:
            obj = ctx['object']
            ctx.update({
                'is_favorited': obj.favorited_by.filter(id=self.request.user.id).exists(),
            })

        return ctx
