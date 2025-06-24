from django.conf import settings


def legalese(request):
    return {
        "DRAWPILE_IMPRESSUM": getattr(settings, "DRAWPILE_IMPRESSUM", None),
        "DRAWPILE_PRIVACY_POLICY": getattr(settings, "DRAWPILE_PRIVACY_POLICY", None),
    }
