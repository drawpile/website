from django.conf.urls import include, url
from rest_framework_nested import routers

from .viewsets import (
    GroupViewSet, GroupMembershipViewSet,
    SubmissionViewSet, SubmissionCommentViewSet
)

router = routers.DefaultRouter()

router.register(r'groups', GroupViewSet)
router.register(r'submissions', SubmissionViewSet)

groups_router = routers.NestedSimpleRouter(router, r'groups', lookup='group')
groups_router.register(r'members', GroupMembershipViewSet, base_name='group-members')

submissions_router = routers.NestedSimpleRouter(router, r'submissions', lookup='submission')
submissions_router.register(r'comments', SubmissionCommentViewSet, base_name='submission-comments')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(groups_router.urls)),
    url(r'^', include(submissions_router.urls)),
]

