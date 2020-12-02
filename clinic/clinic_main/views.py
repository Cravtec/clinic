from django.shortcuts import render
from django.views.generic import ListView

from users import models as users_models
from appointment import models as appointment_models


def index(request):
    doctors = users_models.Doctor.objects.all()
    patients = users_models.Profile.objects.all()
    specializations = users_models.Specialization.objects.all()
    appointments = appointment_models.Appointment.objects.all()
    context = {

        "doctors": doctors,
        "patients": patients,
        "specializations": specializations,
        "appointments": appointments

    }
    return render(request, 'clinic_main/index.html', context)


def about(request):
    return render(request, 'clinic_main/about.html', {})


def contact(request):
    return render(request, 'clinic_main/contact.html', {})


def departments(request):
    return render(request, 'clinic_main/departments.html', {})


def FAQ(request):
    return render(request, 'clinic_main/FAQ.html', {})


def fee(request):
    return render(request, 'clinic_main/fees.html', {})


class DoctorView(ListView):
    template_name = 'clinic_main/about.html'
    model = users_models.Doctor


