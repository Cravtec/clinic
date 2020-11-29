from django import views
from django.http import HttpResponse
from django.shortcuts import render

from clinic.appointment.models import Appointment

from django.views.generic import ListView

class CurrentView1(views.View):
    def get(self, request):
        return render(
            request,
            template_name='call.html',
            context={'appointments': Appointment.objects.all()}
        )

class CurrentView(ListView):
    template_name = 'call.html'
    model = Appointment
