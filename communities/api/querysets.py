from django.db.models import Q

from communities.models import Community, Membership


def get_community_list_queryset(user):
    qs = Community.objects.all()

    # Site admins see everything
    if user.has_perm('communities.change_community'):
        return qs

    # Logged in users can see their own non-visible communities
    if user.is_authenticated:
        my_communities = Membership.objects.filter(
            user=user,
            status__in=Membership.MEMBER_STATUSES
        )
        return qs.filter(
            Q(status=Community.STATUS_ACCEPTED) |
            Q(id__in=my_communities)
        )

    # Other users just see the accepted communities
    return qs.filter(status=Community.STATUS_ACCEPTED)
