from datetime import timedelta
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from django.utils import timezone
from dpusers.models import PendingDeletion


class Command(BaseCommand):
    help = "Execute pending account deletions after 30 days"

    def handle(self, *args, **kwargs):
        thirty_days_ago = timezone.now() - timedelta(days=30)
        user_ids = list(
            PendingDeletion.objects.filter(
                deactivated_at__lte=thirty_days_ago
            ).values_list("user_id", flat=True)
        )
        if user_ids:
            print(f"Deleting {len(user_ids)} user(s): {user_ids}")
            get_user_model().objects.filter(id__in=user_ids).delete()
