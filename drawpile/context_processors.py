from django.conf import settings


def legalese(request):
    return {
        "DRAWPILE_IMPRESSUM": getattr(settings, "DRAWPILE_IMPRESSUM", None),
        "DRAWPILE_PRIVACY_POLICY": getattr(settings, "DRAWPILE_PRIVACY_POLICY", None),
        "DRAWPILE_TOS": getattr(settings, "DRAWPILE_TOS", None),
    }


def fedi(request):
    links = []
    user_agent = request.META.get("HTTP_USER_AGENT", "")
    for c, ls in getattr(settings, "DRAWPILE_FEDI_LINKS", []):
        if not c or c in user_agent:
            links += ls
    return {
        "DRAWPILE_FEDI_LINKS": links,
    }
