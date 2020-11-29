from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from users import forms as users_forms
from users import models as users_models

from django.contrib.auth.models import Group

PATIENT = Group.objects.get(name='patient')
DOCTOR = Group.objects.get(name='patient')
SECRETARY = Group.objects.get(name='patient')


@login_required
def medical_history(request):
    return render(request, 'dashboard/medical_history.html', {})


@login_required
def dashboard(request):
    return render(request, 'dashboard/dashboard.html', {})


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
def profile(request, *args, **kwargs):
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


def register_patient(request):
    if request.method == 'GET':
        return render(request, 'dashboard/create_patient.html')
    if request.method == 'POST':
        form = users_forms.UserCreationForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            user.groups.add(PATIENT)
            users_models.Profile.objects.create(user=user)
            users_models.Address.objects.create(user=user)
            messages.success(request, f'Patient has been registered!')
            # next_url = request.POST.get('next')
            # success_url = reverse('users:login')
            # # if next_url:
            # #     success_url += '?next={}'.format(next_url)
            # return render(request, next_url)
            return redirect(f'dashboard:profile', user.pk)
    else:
        form = users_forms.UserCreationForm()
    return render(request, 'dashboard/create_patient.html', {'form': form})


def register_doctor(request):
    if request.method == 'GET':
        return render(request, 'dashboard/create_doctor.html')
    if request.method == 'POST':
        form = users_forms.UserCreationForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.save()
            user.groups.add(DOCTOR)
            users_models.Doctor.objects.create(user=user)
            users_models.Address.objects.create(user=user)
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = users_forms.UserCreationForm()
    return render(request, 'dashboard/create_doctor.html', {'form': form})


def register_secretary(request):
    if request.method == 'GET':
        return render(request, 'dashboard/create_secretary.html')
    if request.method == 'POST':
        form = users_forms.UserCreationForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            user.is_staff = True
            user.save()
            user.groups.add(SECRETARY)
            users_models.Profile.objects.create(user=user)
            users_models.Address.objects.create(user=user)
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = users_forms.UserCreationForm()
    return render(request, 'dashboard/create_secretary.html', {'form': form})
