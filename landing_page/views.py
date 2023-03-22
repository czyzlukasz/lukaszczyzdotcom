from django.http import HttpResponse
from django.shortcuts import render
from logbook.models import Project, LogEntry

def index(request):
    best_projects = Project.objects.all()[0:3]
    last_log_entries = LogEntry.objects.all()[0:3]
    return render(request, 'landing_page/index.html', context={'projects': best_projects, 'log_entries': last_log_entries})
