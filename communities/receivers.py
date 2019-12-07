from django.dispatch import receiver
from django.db.models.signals import post_delete

from .models import Community, Membership

@receiver(post_delete, sender=Membership)
def transfer_admin_on_deletion(sender, instance, *args, **kwargs):
    if (
        instance.status == Membership.STATUS_ADMIN and
        not Membership.objects.filter(
            community=instance.community,
            status=Membership.STATUS_ADMIN).exists()
    ):

        try:
            next_admin = Membership.objects.filter(
                community=instance.community,
                status__in=(Membership.STATUS_MOD, Membership.STATUS_MEMBER)
                ).order_by('-status', 'joined')[0]
            next_admin.status = Membership.STATUS_ADMIN
            next_admin.save()

        except IndexError:
            # Mark community as orphaned
            c = instance.community
            c.status = Community.STATUS_REJECTED
            c.review_message = ("This community was abandonded by "
                                "its last admin (%s)" % instance.user.username)
            c.save(update_fields=('status', 'review_message'))