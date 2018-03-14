from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
from django.db.models import Q, Count
from django.utils import timezone

from gallery import permissions
from gallery.models import Submission, Comment
from gallery.serializers import (
    SubmissionSerializer, SubmissionDetailSerializer,
    SubmissionCommentSerializer
)

class SubmissionViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.GallerySubmissionPermissions,)
    serializer_class = SubmissionSerializer
    queryset = Submission.objects.all().annotate(favorites=Count('favorited_by')).select_related('picture')
    
    def get_serializer_class(self):
        if self.action == 'list':
            return self.serializer_class

        return SubmissionDetailSerializer

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return self.queryset.filter(Q(is_visible=True) | Q(uploaded_by=self.request.user))
        else:
            return self.queryset.filter(is_visible=True)

    def create(self, request, *args, **kwargs):
        # TODO
        raise NotImplementedError


class SubmissionCommentViewSet(viewsets.ModelViewSet):
    serializer_class = SubmissionCommentSerializer

    def get_queryset(self):
        return Comment.objects.filter(submission_id=self.kwargs['submission_pk'])

    def get_serializer_context(self):
        ctx = super().get_serializer_context()
        ctx.update({
            'submission_id': self.kwargs['submission_pk'],
        })
        return ctx

    def perform_destroy(self, instance):
        instance.deleted = timezone.now()
        instance.save(update_fields=('deleted',))
