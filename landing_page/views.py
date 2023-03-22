from django.http import HttpResponse
from django.shortcuts import render
from logbook.models import Project

def index(request):
    best_projects = Project.objects.all()[0:3]
    return render(request, 'landing_page/index.html', context={'projects': best_projects})
