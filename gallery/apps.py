from django.apps import AppConfig


class GalleryConfig(AppConfig):
    name = 'gallery'

    def ready(self):
        import gallery.signals # register signals

