from django.apps import AppConfig


class CommercialsAppConfig(AppConfig):

    name = "apps.commercials"
    verbose_name = "Application Gestion Commercial"

    def ready(self) -> None:
        from . import signals
