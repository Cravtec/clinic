# from appointment.models import Appointment
from dashboard.forms import CreateAppointmentForm
from datetimerange import DateTimeRange
from dateutil.relativedelta import relativedelta
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.contrib.sites.shortcuts import get_current_site
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
# Create your views here.
from django.views.generic import CreateView, UpdateView

from appointment import filters as appoint_filters
from appointment import models as app_model
from appointment import models as appoint_models

from users import filters as user_filters
from users import forms as users_forms
from users import models as users_models

from .forms import ProfileForm, AddressForm, DoctorForm

PATIENT = Group.objects.get(name='patient')
DOCTOR = Group.objects.get(name='doctor')
SECRETARY = Group.objects.get(name='administration')


@login_required
def medical_history(request):
    appointments = appoint_models.Appointment.objects.filter(profile=request.user.profile.id)
    visits = appoint_models.VisitDescription.objects.filter(appointment__profile=request.user.profile.id)
    context = {'appointments': appointments, 'visits': visits}
    return render(request, 'dashboard/medical_history.html', context)


@login_required
def dashboard(request):
    context = {}
    return render(request, 'dashboard/dashboard.html', context)


@login_required
def doctor(request):
    doctors = users_models.Doctor.objects.all()
    doctor_filter = user_filters.DoctorFilter(request.GET, request=doctors)
    doctors = doctor_filter.qs
    context = {'doctor_filter': doctor_filter,
               'doctors': doctors[:5]}
    return render(request, 'dashboard/doctor.html', context)


@login_required
def patient(request):
    patients = users_models.Profile.objects.all()
    profile_filter = user_filters.ProfileFilter(request.GET, queryset=patients)
    patients = profile_filter.qs
    context = {'profile_filter': profile_filter,
               'patients': patients[:5]}
    return render(request, 'dashboard/patient.html', context)


@login_required
def appointment(request):
    appointments = appoint_models.Appointment.objects.all().order_by('-start_time').order_by('-date')
    appointments_filter = appoint_filters.AppointmentFilter(request.GET, request=appointments)
    appointments = appointments_filter.qs
    context = {'appointments': appointments, 'appointments_filter': appointments_filter}
    return render(request, 'dashboard/appointment.html', context)


@login_required
def calendar(request):
    return render(request, 'dashboard/calendar.html', {})


def register_patient(request):
    if request.method == 'GET':
        return render(request, 'dashboard/create_patient.html')
    if request.method == 'POST':
        form = users_forms.UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            users_models.Profile.objects.create(id=user.pk, user=user)
            users_models.Address.objects.create(id=user.pk, user=user)
            user.groups.add(PATIENT)
            messages.success(request, f'Patient account has been registered! Now fill profile and address forms.')
            return redirect(f'dashboard:profile', user.pk)
    else:
        form = users_forms.UserCreationForm()
    return render(request, 'dashboard/create_patient.html', {'form': form})


# class ProfileUpdateView(LoginRequiredMixin, UpdateView):
#     template_name = 'dashboard/update_profile.html'
#     model = users_models.Profile
#     form_class = ProfileForm
#
#     def get_success_url(self):
#         return reverse('dashboard:update_address', args=(self.object.pk,))
#
#
# class AddressUpdateView(LoginRequiredMixin, UpdateView):
#     template_name = 'dashboard/update_address.html'
#     model = users_models.Address
#     form_class = AddressForm
#     success_url = reverse_lazy('dashboard:dashboard')


def register_doctor(request):
    if request.method == 'GET':
        return render(request, 'dashboard/create_doctor.html')
    if request.method == 'POST':
        form = users_forms.UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, f'Doctor account has been registered! Now fill profile and address forms.')
            user.groups.add(DOCTOR)
            users_models.Address.objects.create(id=user.pk, user=user)
            users_models.Doctor.objects.create(id=user.pk, user=user)
            return redirect(f'dashboard:profile_doctor', user.pk)
    else:
        form = users_forms.UserCreationForm()
    return render(request, 'dashboard/create_doctor.html', {'form': form})


# class DoctorUpdateView(LoginRequiredMixin, UpdateView):
#     template_name = 'dashboard/update_doctor.html'
#     model = users_models.Doctor
#     form_class = DoctorForm
#
#     def get_success_url(self):
#         return reverse('dashboard:update_address', args=(self.object.pk,))


def register_secretary(request):
    if request.method == 'GET':
        return render(request, 'dashboard/create_secretary.html')
    if request.method == 'POST':
        form = users_forms.UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.is_staff = True
            user.save()
            users_models.Address.objects.create(id=user.pk, user=user)
            users_models.Profile.objects.create(id=user.pk, user=user)
            user.groups.add(SECRETARY)
            messages.success(request, f'Secretary account has been registered! Now fill profile and address fields.')
            return redirect(f'dashboard:profile', user.pk)
        else:
            form = users_forms.UserCreationForm()
        return render(request, 'dashboard/create_secretary.html', {'form': form})


@login_required
def profile(request, *args, **kwargs):
    if kwargs:
        profile_instance = users_models.Profile.objects.get(user_id=kwargs['pk'])
        address_instance = users_models.Address.objects.get(user_id=kwargs['pk'])
    else:
        profile_instance = request.user.profile
        address_instance = request.user.address

    if request.method == 'POST':
        p_form = users_forms.ProfileUpdateForm(request.POST, request.FILES, instance=profile_instance)
        a_form = users_forms.AddressUpdateForm(request.POST, instance=address_instance)
        if p_form.is_valid() and a_form.is_valid():
            p_form.save()
            a_form.save()
            messages.success(request, f'Profile has been updated!')
            return redirect('dashboard:dashboard')
    else:
        p_form = users_forms.ProfileUpdateForm(instance=profile_instance)
        a_form = users_forms.AddressUpdateForm(instance=address_instance)
    context = {
        'p_form': p_form,
        'a_form': a_form
    }
    return render(request, 'dashboard/profile.html', context)


@login_required
def profile_doctor(request, *args, **kwargs):
    if kwargs:
        doctor_instance = users_models.Doctor.objects.get(user_id=kwargs['pk'])
        doctor_address_instance = users_models.Address.objects.get(user_id=kwargs['pk'])
    else:
        doctor_instance = request.user.doctor
        doctor_address_instance = request.user.address

    if request.method == 'POST':
        d_form = users_forms.DoctorUpdateForm(request.POST, request.FILES, instance=doctor_instance)
        a_form = users_forms.AddressUpdateForm(request.POST, instance=doctor_address_instance)
        if d_form.is_valid() and a_form.is_valid():
            d_form.save()
            a_form.save()
            messages.success(request, f'Doctors profile has been updated!')
            return redirect('dashboard:dashboard')
    else:
        d_form = users_forms.DoctorUpdateForm(instance=doctor_instance)
        a_form = users_forms.AddressUpdateForm(instance=doctor_address_instance)
    context = {
        'd_form': d_form,
        'a_form': a_form
    }
    return render(request, 'dashboard/profile_doctor.html', context)


# @login_required
# def app_cal(request):
#     return render(request, 'appointment/app_cal.html', {})


@login_required
def check_hours(request, query=None):
    print(request.GET["datechoosen"])
    picked_date = request.GET["datechoosen"]
    doctor_id = request.GET["id_doctor"]

    all_appointments = Appointment.objects.filter(date=picked_date, doctor_id=doctor_id)

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
