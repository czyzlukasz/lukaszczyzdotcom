from django.contrib import admin

from .models import Project, LogEntry


admin.site.register(Project)
admin.site.register(LogEntry)