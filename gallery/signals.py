from django.db.models.signals import post_delete
from django.dispatch import receiver

from .models import Group, GroupMembership

import logging
logger = logging.getLogger(__name__)

@receiver(post_delete, sender=GroupMembership)
def on_groupmembership_deleted(sender, instance, **kwargs):
    if not GroupMembership.objects.filter(
            group_id=instance.group_id,
            status__in=GroupMembership.MEMBER_STATUSES
            ).exists():
        logger.info("Last member of group #%d left: deleting", instance.group_id)
        Group.objects.filter(id=instance.group_id).delete()

    elif instance.status == GroupMembership.STATUS_MOD \
            and not GroupMembership.objects.filter(
                group_id=instance.group_id,
                status=GroupMembership.STATUS_MOD
                ).exists():
        # Group has no more moderators!
        # Typically, the user should have designated some other user as a
        # moderator before leaving, but this situation can happen if the user
        # deletes their account without passing on mod status first. Since a
        # group must have at least one moderator, we just make the oldest
        # member a moderator.
        m = GroupMembership.objects.filter(group_id=instance.group_id, status=GroupMembership.STATUS_MEMBER).order_by('id')[0]
        logger.info("Last mod of group #%d left: granting mod status to user #%d", instance.group_id, m.user_id)
        m.status = GroupMembership.STATUS_MOD
        m.save(update_fields=('status',))



