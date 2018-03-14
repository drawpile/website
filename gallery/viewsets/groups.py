from rest_framework.exceptions import ValidationError
from rest_framework import viewsets
from django.db.models import Count
from django.db import IntegrityError

from gallery import permissions
from gallery.models import Group, GroupMembership
from gallery.serializers import GroupSerializer, GroupMembershipSerializer

class GroupViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.GalleryGroupPermissions,)
    serializer_class = GroupSerializer
    queryset = Group.objects.all().annotate(members=Count('groupmembership'))
    lookup_field = 'slug'


class GroupMembershipViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.GalleryGroupMembershipPermissions,)
    serializer_class = GroupMembershipSerializer

    def get_queryset(self):
        return GroupMembership.objects.filter(group__slug=self.kwargs['group_slug'])

    def create(self, request, *args, **kwargs):
        g = Group.objects.get(slug=self.kwargs['group_slug'])
        try:
            m = GroupMembership.objects.create(
                group=g,
                user=request.user,
                status=GroupMembership.STATUS_PENDING if g.approve_joins else GroupMembership.STATUS_MEMBER
            )
        except IntegrityError:
            raise ValidationError({'error': 'You are already in this group'}, 'already-in-group')

        s = GroupMembershipSerializer(m)
        return Response(s.data, status=status.HTTP_201_CREATED)
