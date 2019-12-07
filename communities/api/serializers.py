from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.utils.encoding import smart_str

from communities.models import Community, Membership
from dpauth.models import Username

class CommunityListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        read_only_fields = (
            'slug', 'status', 'title', 'short_description', 'badge'
        )
        fields = read_only_fields


class CommunityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Community
        read_only_fields = (
            'created', 'slug'
        )
        fields = read_only_fields + (
            'title', 'short_description', 'full_description', 'badge',
            'rules', 'group_policy', 'memberlist_visibility',
            'drawpile_server', 'list_server', 'homepage',
            'guest_policy', 'account_host', 'require_group_membership',
        )


class UserField(serializers.RelatedField):
    default_error_messages = {
        'does_not_exist': 'User with the name {value} not found',
        'invalid': 'Invalid value.',
    }

    def __init__(self, *args, **kwargs):
        if not kwargs.get('read_only', False):
            kwargs['queryset'] = get_user_model().objects.all()

        super().__init__(*args, **kwargs)

    def to_internal_value(self, data):
        try:
            un = Username.getByName(data)
        except (TypeError, ValueError):
            self.fail('invalid')
            return None

        if un is None:
            self.fail('does_not_exist', value=smart_str(data))
            return None

        return un.user

    def to_representation(self, obj):
        return obj.username


class InviteMemberSerializer(serializers.Serializer):
    user = UserField(label="Invite User")

    def validate_user(self, value):
        if Membership.objects.filter(
            user=value,
            community=self.context.get('community')
        ).exists():
            raise serializers.ValidationError("This user is already a member")
        return value

    def create(self, validated_data):
        return Membership.objects.create(
            user=validated_data['user'],
            community=self.context['community'],
            status=Membership.STATUS_INVITED
        )


class JoinSerializer(serializers.Serializer):
    pass


class MembershipSerializer(serializers.ModelSerializer):
    user = UserField(read_only=True)
    joined = serializers.DateTimeField(format='%Y-%m-%d', read_only=True)

    def __init__(self, *args, **kwargs):
        show_ban = kwargs.pop('show_ban', True)
        super().__init__(*args, **kwargs)

        if (
            isinstance(self.instance, Membership) and
            self.instance.status == Membership.STATUS_INVITED
        ):
            # Users can only join the group of their own volition
            statuses = (Membership.STATUS_INVITED, Membership.STATUS_BANNED)
            show_ban = False
            if self.instance.user == self.context['request'].user:
                statuses = statuses + (Membership.STATUS_MEMBER,)

            self.fields['status'].choices = [
                (k, v) for k, v in self.fields['status'].choices.items()
                if k in statuses
            ]

        if not show_ban:
            self.fields.pop('ban_reason')

    class Meta:
        model = Membership
        read_only_fields = ('user', 'joined',)
        fields = read_only_fields + ('status', 'ban_reason',)


class AbuseReportSerializer(serializers.Serializer):
    comment = serializers.CharField()
