from django.contrib import admin
from api import models


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Agent)
class AgentAdmin(admin.ModelAdmin):
    pass
