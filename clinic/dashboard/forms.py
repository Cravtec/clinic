from datetime import datetime
from django import forms

from users import models as users_models
from appointment import models as app_model


class ProfileForm(forms.ModelForm):
    class Meta:
        model = users_models.Profile
        fields = ['first_name', 'mid_name', 'last_name', 'gender', 'birth_date',
                  'nationality', 'phone_number', 'pesel', 'image']

    birth_date = forms.DateField(
        required=False,
        widget=forms.SelectDateWidget(
            empty_label=("Year", "Month", "Day"),
            years=range(datetime.now().year - 120, datetime.now().year + 1)
        ))


class DoctorForm(forms.ModelForm):
    class Meta:
        model = users_models.Doctor
        fields = '__all__'


class AddressForm(forms.ModelForm):
    class Meta:
        model = users_models.Address
        fields = ['country', 'home_number', 'street', 'address', 'town', 'state', 'postal_code']


class SpecializationForm(forms.ModelForm):
    class Meta:
        model = users_models.Specialization
        fields = '__all__'


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
