from django.apps import AppConfig


class DpusersConfig(AppConfig):
    name = 'dpusers'

    def ready(self):
        import dpusers.receivers # imported for side effect
