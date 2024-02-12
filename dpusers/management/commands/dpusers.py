from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import timedelta

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
        else:
            raise CommandError("Action must be one of: purge-unused, delete-pending")

    def __purge_unused(self, older):
        if older < 1:
            raise CommandError("Purge cutoff should be at least one day")

        cutoff = timezone.now() - timedelta(days=older)
        User = get_user_model()
        unused_accounts = User.objects.filter(last_login__lt=cutoff)

        if self.dryrun:
            print(
                "Would delete {} accounts that have not logged in since {}".format(
                    unused_accounts.count(), cutoff
                )
            )
        else:
            deleted_count, deleted_types = unused_accounts.delete()
            if self.verbosity > 1:
                print(
                    "Deleted {} accounts that have not logged in since {}".format(
                        deleted_count, cutoff
                    )
                )


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
