from django.apps.config import AppConfig


class HRManagmentAppConfig(AppConfig):

    name = "apps.hr_managments"
    verbose_name = "HR Managements Application"

    def ready(self) -> None:
        return super().ready()
