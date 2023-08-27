from django.conf import settings
from django.db import models
from autoslug import AutoSlugField
from martor.models import MartorField


class Project(models.Model):
    project_name = models.CharField(max_length=500)
    project_description = MartorField()
    fanciness = models.IntegerField(default=0)
    public = models.BooleanField(default=False, null=True)
    image = models.ImageField(null=True, blank=True)

    slug = AutoSlugField(populate_from='project_name', unique=True)

    def __str__(self) -> str:
        return f"{self.project_name}"


class LogEntry(models.Model):
    class Meta:
        ordering = ["-publish_date"]

    project = models.ForeignKey(Project, on_delete=models.PROTECT)
    entry_name = models.CharField(max_length=500)
    entry_description = models.CharField(max_length=500, null=True)
    text = MartorField()
    publish_date = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=False, null=True)

    slug = AutoSlugField(populate_from='entry_name', unique=True)

    def __str__(self) -> str:
        return f"Log {self.entry_name} of project {self.project.project_name}"


class LogPhoto(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField()
    description = models.TextField()
