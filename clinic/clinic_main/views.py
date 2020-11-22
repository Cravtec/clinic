from django.shortcuts import render


def index(request):
    return render(request, 'clinic_main/index.html', {})


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
