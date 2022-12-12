from django.apps import AppConfig


class StockConfig(AppConfig):

    name = "apps.stock"
    verbose_name = "Stock Application"

    def ready(self):
        from . import signals
