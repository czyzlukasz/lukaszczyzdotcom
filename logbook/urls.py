from django.urls import path
from . import views

app_name = 'logbook'

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/<str>', views.ProjectView.as_view(), name='project')
]
