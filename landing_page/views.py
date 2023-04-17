from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.contrib.messages.views import SuccessMessageMixin

from landing_page.models import ContactMessage
from logbook.models import Project, LogEntry

def index(request):
    best_projects = Project.objects.all()[0:3]
    last_log_entries = LogEntry.objects.all()[0:3]
    return render(request, 'landing_page/index.html', context={'projects': best_projects, 'log_entries': last_log_entries})

def privacy_policy(request):
    return render(request, 'landing_page/privacy_policy.html')

class ContactMessageCreateView(SuccessMessageMixin, CreateView):
    model = ContactMessage
    fields = ('name', 'email', 'text', 'accepted_terms')
    success_url = reverse_lazy('landing_page:contact')
    success_message = "Thanks! I'll contact You as soon as possible."

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['accepted_terms'].required = True
        form.fields['accepted_terms'].label = "I agree to the privacy policy."
        return form
