from django.urls import path
from . import views

app_name = 'landing_page'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.ContactMessageCreateView.as_view(), name='contact')
]
