from django.apps import AppConfig


class TasksConfigApp(AppConfig):

    name = 'apps.tasks'
    verbose_name = 'Tasks Application'

    def ready(self):
        from . import signals
