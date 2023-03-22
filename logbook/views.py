from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Project


def index(request):
    return HttpResponse('elo')

class ProjectView(DetailView):
    model = Project

    context_object_name = 'project'