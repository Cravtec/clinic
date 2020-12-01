from datetimerange import DateTimeRange
from dateutil.relativedelta import relativedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from appointment import models as app_model
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView
from users import forms as users_forms

from appointment.models import Appointment

from dashboard.forms import CreateAppointmentForm


@login_required
def dashboard(request):
    return render(request, 'dashboard/dash.html', {})


@login_required
def profile(request):
    if request.method == 'POST':
        p_form = users_forms.ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        a_form = users_forms.AddressUpdateForm(request.POST, instance=request.user.address)
        if p_form.is_valid() and a_form.is_valid():
            p_form.save()
            a_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('dashboard:profile')
    else:
        p_form = users_forms.ProfileUpdateForm(instance=request.user.profile)
        a_form = users_forms.AddressUpdateForm(instance=request.user.address)
    context = {
        'p_form': p_form,
        'a_form': a_form
    }
    return render(request, 'dashboard/profile.html', context)


@login_required
def profile_edit(request):
    return render(request, 'dashboard/profile_edit.html', {})


@login_required
def doctor(request):
    return render(request, 'dashboard/doctor.html', {})


@login_required
def appointment(request):
    return render(request, 'dashboard/appointment.html', {})


@login_required
def calendar(request):
    return render(request, 'dashboard/calendar.html', {})


@login_required
def medical_history(request):
    return render(request, 'dashboard/medical_history.html', {})


@login_required
def app_cal(request):
    return render(request, 'appointment/app_cal.html', {})


@login_required
def check_hours(request, query=None):
    # print(request.GET["datechoosen"])
    picked_date = request.GET["datechoosen"]
    doctor_id = request.GET["id_doctor"]

    if isinstance(doctor_id, int):
        all_appointments = Appointment.objects.filter(date=picked_date, doctor_id=doctor_id)
    else:
        all_appointments = Appointment.objects.filter(date=picked_date)

    current_appointments = []
    time_list = []
    time_to_display = []

    for appointment in all_appointments:
        if appointment.start_time.hour < 10:
            hours = '0' + str(appointment.start_time.hour)
        else:
            hours = appointment.start_time.hour

        if appointment.start_time.minute == 0:
            minutes = '00'
        else:
            minutes = appointment.start_time.minute
        current_appointments.append(f'{hours}:{minutes}')

    time_range = DateTimeRange("2015-01-01T09:00:00", "2015-01-01T17:00:00")
    for value in time_range.range(relativedelta(minutes=30)):
        time_list.append(str(value.time())[0:5])

    for current_time in time_list:
        if current_time not in current_appointments:
            time_to_display.append(current_time)

    result = {i: {"time": time_to_display[i]} for i in range(0, len(time_to_display))}
    return JsonResponse(result)


class CreateAppointmentView(CreateView):
    template_name = "dashboard/calendar.html"
    model = app_model.Appointment

    form_class = CreateAppointmentForm

    success_url = reverse_lazy('dashboard:calendar')
