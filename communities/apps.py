from django.apps import AppConfig


class CommunitiesConfig(AppConfig):
    name = 'communities'

    def ready(self):
        import communities.receivers  # imported for side effect