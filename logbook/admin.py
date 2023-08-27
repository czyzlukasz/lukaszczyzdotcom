from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from martor.widgets import AdminMartorWidget

from .models import Project, LogEntry, LogPhoto


class ProjectAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


class LogEntryAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': AdminMartorWidget},
    }


class LogPhotoAdmin(admin.ModelAdmin):
    list_display = ('name', 'image_preview', 'description')

    @staticmethod
    def image_preview(obj):
        return format_html(f'<img src="{obj.image.url}" style="max-width:100%;" />')


admin.site.register(Project, ProjectAdmin)
admin.site.register(LogEntry, LogEntryAdmin)
admin.site.register(LogPhoto, LogPhotoAdmin)
