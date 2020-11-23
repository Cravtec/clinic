from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Create your views here.
from users import forms as users_forms


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


def profile_edit(request):
    return render(request, 'dashboard/profile_edit.html', {})


def doctor(request):
    return render(request, 'dashboard/doctor.html', {})


def appointment(request):
    return render(request, 'dashboard/appointment.html', {})


def calendar(request):
    return render(request, 'dashboard/calendar.html', {})
