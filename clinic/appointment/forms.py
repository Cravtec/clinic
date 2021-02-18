from django import forms

from .models import *


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = ['amount', 'status']


class VisitDescriptionForm(forms.ModelForm):
    class Meta:
        model = VisitDescription
        fields = ['symptoms', 'diagnose', 'treatment']


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = ['name', 'description']
