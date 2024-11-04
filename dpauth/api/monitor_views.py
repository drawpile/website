from django.conf import settings
from django.core.cache import cache
from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from django.http import HttpResponse
from django.views import View
from dpauth.models import MonitorWordList
import json


class MonitorConfigView(View):
    def get(self, request, monitorkey):
        if monitorkey not in settings.DRAWPILE_MONITOR_KEYS:
            return HttpResponse(
                b'{"error":"forbidden"}', status=403, content_type="application/json"
            )
        return HttpResponse(
            self.__build_response_body(), status=200, content_type="application/json"
        )

    def __build_response_body(self):
        config = {
            "config": settings.DRAWPILE_MONITOR_CONFIG,
            "messages": settings.DRAWPILE_MONITOR_MESSAGES,
        }
        for wordlist in MonitorWordList.objects.all():
            config[wordlist.list_type] = list(wordlist.words.splitlines())
        return json.dumps(config, separators=(",", ":")).encode("utf-8")
