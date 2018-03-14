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


@method_decorator(login_required, name='dispatch')
class ChangeFavoriteComment(View):
    def post(self, request, pk):
        s = get_object_or_404(Submission, pk=pk, is_visible=True)
        if self.request.POST['action'] == 'favorite':
            Favorited.objects.create(
                submission=s,
                user=self.request.user
            )

        elif self.request.POST['action'] == 'unfavorite':
            Favorited.objects.filter(submission=s, user=self.request.user).delete()

        return HttpResponse(status=204)


@method_decorator(login_required, name='dispatch')
class CommentSubmission(View):
    def post(self, request, pk):
        s = get_object_or_404(Submission, pk=pk)
        if not s.can_comment(self.request.user):
            raise Http404

        text = request.POST.get('comment', '').strip()
        if text:
            Comment.objects.create(
                submission=s,
                user=request.user,
                text=text
            )
        
        return redirect(s.get_absolute_url() + "#comments")


@method_decorator(login_required, name='dispatch')
class EditComment(View):
    def delete(self, request, submission_pk, pk):
        """Delete a comment"""
        s = get_object_or_404(Submission, pk=submission_pk)
        c = get_object_or_404(Comment, pk=pk, submission=s)
        if c.can_delete(request.user):
            c.deleted = timezone.now()
            c.save(update_fields=('deleted',))
            return HttpResponse(status=204)

        else:
            return HttpResponse(status=400)
    
    def put(self, request, submission_pk, pk):
        """Undelete a comment"""
        s = get_object_or_404(Submission, pk=submission_pk)
        c = get_object_or_404(Comment, pk=pk, submission=s)
        if c.can_undelete(request.user):
            c.deleted = None
            c.save(update_fields=('deleted',))
            
            return render(request, 'gallery/__submission_comment.html', {
                'object': s,
                'comment': c,
            })

        else:
            return HttpResponse(status=400)


@method_decorator(login_required, name='dispatch')
class SubmitView(FormView):
    template_name = 'gallery/submit.html'
    form_class = ContentSubmissionForm
    
    def get_context_data(self, **kwargs):
        uploaded = Submission.get_total_size(self.request.user)
        quota =  settings.UPLOAD_QUOTA * 1024 * 1024

        ctx = super().get_context_data(**kwargs)
        ctx.update({
            'is_over_quota': uploaded >= quota,
            'available': int(max(0, (quota - uploaded) / quota) * 100),
        })
        return ctx

    def post(self, request, *args, **kwargs):
        if Submission.get_total_size(self.request.user) > (settings.UPLOAD_QUOTA * 1024 * 1024):
            return HttpResponse(400)
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        upload = form.cleaned_data['submission']
        with transaction.atomic():
            s = Submission.objects.create(
                uploaded_by=self.request.user,
                submission_type=Submission.TYPE_PICTURE,
                thumbnail=pictures.make_thumbnail(upload)
                )
            
            Picture.objects.create(
                submission=s,
                downscaled=pictures.downscale_if_necessary(upload),
                fullsize=upload,
                filesize=upload.size
                )
            
            return redirect('gallery:edit-submission', pk=s.id)


@method_decorator(login_required, name='dispatch')
class EditSubmission(UpdateView):
    template_name = 'gallery/edit_submission.html'
    form_class = EditSubmissionForm
    queryset = Submission.objects.all()
    
    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        if not obj.can_edit(self.request.user):
            raise Http404
        return obj
    
    def get_success_url(self):
        return self.object.get_absolute_url()
    
    def post(self, request, *args, **kwargs):
        if request.POST['action'] == 'delete':
            self.get_object().delete()
            return redirect('gallery:userpage', pk=request.user.id)
        
        return super().post(request, *args, **kwargs)

