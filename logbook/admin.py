from django.contrib import admin
from django.db import models

from martor.widgets import AdminMartorWidget

from .models import Project, LogEntry

class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

class LogEntryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }

admin.site.register(Project, ProjectAdmin)
admin.site.register(LogEntry, LogEntryAdmin)