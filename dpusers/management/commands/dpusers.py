from datetime import timedelta
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError
from django.utils import timezone
from dpusers.models import PendingDeletion
import re


class Command(BaseCommand):
    help = "Manage Drawpile.net user accounts"

    def add_arguments(self, parser):
        parser.add_argument("action", type=str)
        parser.add_argument("--older-than", type=str, dest="older", required=True)
        parser.add_argument("--dry-run", action="store_true", dest="dryrun")

    def handle(self, *args, **kwargs):
        action = kwargs["action"]
        self.dryrun = kwargs["dryrun"]
        self.verbosity = kwargs["verbosity"]

        if action == "purge-unused":
            self.__purge_unused(_parse_datedelta_string(kwargs["older"]))
        elif action == "delete-pending":
            self.__delete_pending(_parse_datedelta_string(kwargs["older"]))
        else:
            raise CommandError("Action must be one of: purge-unused, delete-pending")

    def __purge_unused(self, older):
        if older < 1:
            raise CommandError("Purge cutoff should be at least one day")

        cutoff = timezone.now() - timedelta(days=older)
        User = get_user_model()
        unused_accounts = User.objects.filter(last_login__lt=cutoff)

        if self.dryrun:
            user_ids = list(unused_accounts.values_list("id", flat=True))
            print(
                f"Would delete {len(user_ids)} account(s) that have not logged in since {cutoff}: {user_ids}"
            )
        else:
            deleted_count, deleted_types = unused_accounts.delete()
            min_verbosity = 1 if deleted_count > 0 else 2
            if self.verbosity > min_verbosity:
                print(
                    f"Deleted {deleted_count} account(s) that have not logged in since {cutoff}"
                )

    def __delete_pending(self, older):
        if older < 30:
            raise CommandError("Delete pending cutoff should be at least 30 days")
        cutoff = timezone.now() - timedelta(days=older)
        user_ids = list(
            PendingDeletion.objects.filter(deactivated_at__lt=cutoff).values_list(
                "user_id", flat=True
            )
        )
        if self.dryrun:
            print(
                f"Would delete {len(user_ids)} account(s) pending deletion since {cutoff}: {user_ids}"
            )
        elif user_ids:
            deleted_count, deleted_types = (
                get_user_model().objects.filter(id__in=user_ids).delete()
            )
            if self.verbosity > 1:
                print(
                    f"Deleted {deleted_count} account(s) pending deletion since {cutoff}"
                )
        elif self.verbosity > 2:
            print(f"No accounts pending deletion since {cutoff}")


def _parse_datedelta_string(datestr):
    m = re.match(r"^(\d+)\s*(year|month|day)s$", datestr)
    if not m:
        raise CommandError("Unparseable date string: " + datestr)

    n = int(m.group(1))
    unit = m.group(2)
    if unit == "year":
        n = n * 365
    elif unit == "month":
        n = n * 31

    return n
