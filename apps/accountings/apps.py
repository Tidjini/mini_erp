from django.apps import AppConfig


class ComptabiliteConfigApp(AppConfig):

    name = "apps.accountings"
    verbose_name = "Accountings Application"

    def ready(self):
        from . import signals
