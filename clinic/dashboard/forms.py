from appointment import models as app_model
from django import forms




class CreateAppointmentForm(forms.ModelForm):

    class Meta:
        model = app_model.Appointment
        fields = ("doctor", "profile", "date", "start_time")


