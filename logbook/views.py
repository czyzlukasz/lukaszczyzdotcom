from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Project, LogEntry


def projects_view(request):
    all_projects = Project.objects.filter(public = True)
    return render(request, 'logbook/projects.html', context={'projects': all_projects})


class ProjectView(DetailView):
    model = Project
    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        log_entries = LogEntry.objects.filter(public = True).filter(project = context['project']).order_by('publish_date')
        context['log_entries'] = log_entries
        return context
    
class LogEntryView(DetailView):
    model = LogEntry
    context_object_name = 'log_entry'
