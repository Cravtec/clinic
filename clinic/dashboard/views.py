from django.shortcuts import render

# Create your views here.

def dashboard(request):
    return render(request, 'dashboard/dash.html', {})


def profile(request):
    return render(request, 'dashboard/profile.html', {})


def profile_edit(request):
    return render(request, 'dashboard/profile_edit.html', {})


def doctor(request):
    return render(request, 'dashboard/doctor.html', {})


def appointment(request):
    return render(request, 'dashboard/appointment.html', {})


def calendar(request):
    return render(request, 'dashboard/calendar.html', {})
