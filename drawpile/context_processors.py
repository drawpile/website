from django.conf import settings


def impressum(request):
    return {"DRAWPILE_IMPRESSUM": getattr(settings, "DRAWPILE_IMPRESSUM", None)}
