from django.conf import settings
from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.utils.timezone import now
from django.views import View
from dpauth.models import Ban, BanIpRange, BanSystemIdentifier, BanUser
import json


class ExtBanView(View):
    CACHE_VIEW_KEY = "drawpile_dpauth_extbanview"

    def get(self, request, extbankey):
        if extbankey not in settings.DRAWPILE_EXT_BANS_KEYS:
            return HttpResponse(
                b'{"error":"forbidden"}', status=403, content_type="application/json")

        status = 200
        etag, body = cache.get(ExtBanView.CACHE_VIEW_KEY, (None, None))
        if etag:
            if request.headers.get("If-None-Match") == etag:
                status = 304
                body = b""
        else:
            # Sufficiently unique for our single-process, single-node usage.
            etag = f"{id(cache):x}g{int(now().timestamp()):x}"
            body = self.__build_response_body()
            cache.set(ExtBanView.CACHE_VIEW_KEY, (etag, body), timeout=None)
        return HttpResponse(
            body, status=status, content_type="application/json", headers={"ETag": etag})

    def __build_response_body(self):
        extbans = {
            "bans": [ExtBanView.__ban_to_json(ban) for ban in Ban.objects.all()],
        }
        return json.dumps(extbans, separators=(',', ':')).encode("utf-8")

    @staticmethod
    def __ban_to_json(ban):
        json = {
            "id": ban.id,
            "expires": ban.expires.strftime("%Y-%m-%d 23:59:59"),
            "comment": ban.comment,
            "ips": [
                ExtBanView.__iprange_to_json(ban, iprange)
                    for iprange in ban.baniprange_set.all()
                    if not iprange.excluded
            ],
            "ipsexcluded": [
                ExtBanView.__iprange_to_json(ban, iprange)
                    for iprange in ban.baniprange_set.all()
                    if iprange.excluded
            ],
            "system": ExtBanView.__sids_to_json(ban),
            "users": ExtBanView.__users_to_json(ban),
        }
        if ban.reason:
            json["reason"] = ban.reason
        return json

    @staticmethod
    def __iprange_to_json(ban, iprange):
        json = {
            "from": iprange.from_ip,
            "to": iprange.to_ip if iprange.to_ip else iprange.from_ip,
        }
        if not iprange.excluded and ban.reaction_includes_ipbans \
                and ban.reaction != Ban.Reactions.NORMAL:
            json["reaction"] = ban.reaction
        return json

    @staticmethod
    def __sids_to_json(ban):
        sids = ban.bansystemidentifier_set.values_list("identifier", flat=True)
        if sids:
            json = {"sids": list(sids)}
            if ban.reaction != Ban.Reactions.NORMAL:
                json["reaction"] = ban.reaction
            return [json]
        else:
            return []

    @staticmethod
    def __users_to_json(ban):
        user_ids = ban.banuser_set.values_list("user_id", flat=True)
        if user_ids:
            json = {"ids": list(user_ids)}
            if ban.reaction != Ban.Reactions.NORMAL:
                json["reaction"] = ban.reaction
            return [json]
        else:
            return []

@receiver(post_save, sender=Ban)
@receiver(post_delete, sender=Ban)
@receiver(post_save, sender=BanIpRange)
@receiver(post_delete, sender=BanIpRange)
@receiver(post_save, sender=BanSystemIdentifier)
@receiver(post_delete, sender=BanSystemIdentifier)
@receiver(post_save, sender=BanUser)
@receiver(post_delete, sender=BanUser)
def _purge_extban_cache(**_kwargs):
    cache.delete(ExtBanView.CACHE_VIEW_KEY)
