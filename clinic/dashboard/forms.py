from appointment import models as app_model
from django import forms


class CreateAppointmentForm(forms.ModelForm):
    class Meta:
        model = app_model.Appointment
        fields = ("doctor", "profile", "date", "start_time")
        widgets = {
            "doctor": forms.Select(
                attrs={'class': 'form-control form-control-lg id_doctor', 'onclick': 'checkTime()'}),
            "profile": forms.Select(attrs={'class': 'form-control form-control-lg'}),
            'date': forms.HiddenInput(attrs={'class': 'form-control form-control-lg'}),
            'start_time': forms.HiddenInput(
                attrs={'class': 'form-control form-control-lg'})

        }
