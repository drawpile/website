from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime
from dpauth.models import Ban, BanIpRange
from django.db import transaction
import json
import ipaddress
import re


class Command(BaseCommand):
    help = "Import external bans"

    def add_arguments(self, parser):
        parser.add_argument("path", type=str)

    def handle(self, *args, **kwargs):
        with open(kwargs["path"]) as f:
            input_bans = json.load(f)

        with transaction.atomic():
            for input_ban in input_bans:
                ban = Ban(comment=input_ban["comment"])

                expires = parse_datetime(input_ban["expires"])
                if expires.year < 2030:
                    ban.expires = expires

                try:
                    ban.reason = input_ban["reason"]
                except KeyError:
                    pass

                ban.save()

                for ip_range in input_ban["bans"]:
                    raw_ip, subnet = self._demangle_ip(
                        ip_range["ip"], ip_range["subnet"]
                    )
                    if subnet == 0:
                        address = ipaddress.ip_address(raw_ip)
                        ban_range = BanIpRange(from_ip=str(address))
                    else:
                        network = ipaddress.ip_network((raw_ip, subnet), strict=False)
                        ban_range = BanIpRange(
                            from_ip=str(network.network_address),
                            to_ip=str(network.broadcast_address),
                        )
                    ban_range.ban = ban
                    ban_range.save()

    IPV4_REGEX = re.compile(r"^::ffff:([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)$")

    @staticmethod
    def _demangle_ip(raw_ip, subnet):
        match = Command.IPV4_REGEX.search(raw_ip)
        if match:
            return (match[1], 0 if subnet <= 0 or subnet >= 128 else subnet - 96)
        else:
            return (raw_ip, subnet)
