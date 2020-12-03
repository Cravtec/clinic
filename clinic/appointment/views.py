from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages
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


# @login_required
# def create_visit(request, *args, **kwargs):
#     if Payment.objects.filter(id=kwargs['pk']):
#         Payment.objects.create(appointment_id=kwargs['pk'])
#     if VisitDescription.objects.filter(id=kwargs['pk']):
#         VisitDescription.objects.create(appointment_id=kwargs['pk'])
#     if Prescription.objects.filter(id=kwargs['pk']):
#         Prescription.objects.create(appointment_id=kwargs['pk'])
#
#     visit_instance = Appointment.objects.get(id=kwargs['pk'])
#
#     if request.method == 'POST':
#         payment_form = PaymentForm(request.POST, instance=visit_instance)
#         print(payment_form)
#         visit_form = VisitDescriptionForm(request.POST, instance=visit_instance)
#         print(visit_form)
#         presc_form = Prescription(request.POST, instance=visit_instance)
#         if payment_form.is_valid() and visit_form.is_valid() and presc_form.is_valid():
#             payment_form.save()
#             visit_form.save()
#             presc_form.save()
#             messages.success(request, f'Appointment data has been stored successfully!')
#             return redirect('dashboard:dashboard')
#         else:
#             payment_form = PaymentForm(instance=visit_instance)
#             visit_form = VisitDescriptionForm(instance=visit_instance)
#             presc_form = Prescription(instance=visit_instance)
#
#         context = {
#             'payment_form': payment_form,
#             'visit_form': visit_form,
#             'presc_form': presc_form,
#         }
#         return render(request, 'dashboard/create_visit.html', context)

