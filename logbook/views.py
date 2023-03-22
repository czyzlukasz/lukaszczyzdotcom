from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Project, LogEntry


def index(request):
    return HttpResponse('elo')

class ProjectView(DetailView):
    model = Project

    context_object_name = 'project'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        log_entries = LogEntry.objects.filter(project = context['project'])
        context['log_entries'] = log_entries
        return context