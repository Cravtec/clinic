from django import forms

from .models import *


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__'


class PaymentForm(forms.ModelForm):
    class Meta:
        model = Payment
        fields = '__all__'


class VisitDescriptionForm(forms.ModelForm):
    class Meta:
        model = VisitDescription
        fields = '__all__'


class PrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        fields = '__all__'

