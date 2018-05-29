from rest_framework import serializers

from gallery.models import Group, GroupMembership

class GroupSerializer(serializers.ModelSerializer):
    members = serializers.IntegerField(read_only=True)

    class Meta:
        model = Group
        read_only_fields = ('slug', 'title', 'members', 'created')
        fields = read_only_fields + ('logo', 'description', 'server_address', 'website', 'approve_joins')


class GroupMembershipSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        model = GroupMembership
        read_only_fields = ('id', 'user', 'joined')
        fields = read_only_fields + ('status',)
