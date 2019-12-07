from django.db.models import Q

from communities.models import Community


def get_community_list_queryset(user):
    qs = Community.objects.all()

    # Site admin level access
    if user.has_perm('communities.change_community'):
        return qs

    # Logged in users can see their own non-visible communities
    if user.is_authenticated:
        qs = qs.filter(
            Q(status=Community.STATUS_ACCEPTED) |
            Q(users=user)
            ).distinct()
        return qs

    # Other users just see the accepted communities
    return qs.filter(status=Community.STATUS_ACCEPTED)
