from django.urls import path
from . import views

app_name = 'logbook'

urlpatterns = [
    path('projects/', views.projects_view, name='projects'),
    path('<slug:slug>/', views.ProjectView.as_view(), name='project'),
    path('log/<slug:slug>/', views.LogEntryView.as_view(), name='log_entry')
]
