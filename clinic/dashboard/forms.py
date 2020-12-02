from datetime import datetime

from django import forms
from users import models as users_models


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
