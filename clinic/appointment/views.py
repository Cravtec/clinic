from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib.messages.views import SuccessMessageMixin

from .forms import *
from .models import Appointment


class AppointmentDeleteView(LoginRequiredMixin, DeleteView):
    model = Appointment
    template_name = 'dashboard/delete_confirm_appointment.html'
    success_url = reverse_lazy('dashboard:appointments')


class AppointmentUpdateView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    template_name = 'dashboard/update_appointment.html'
    model = Appointment
    form_class = AppointmentForm
    success_url = reverse_lazy('dashboard:appointments')
    success_message = 'Appointment updated successfully!'


@login_required
def visit_form(request):
    pass