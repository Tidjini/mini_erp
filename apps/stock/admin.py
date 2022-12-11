from django.contrib import admin

from . import models

class UniteAdmin(admin.ModelAdmin):
    pass


admin.site.register(models.Unite, UniteAdmin)