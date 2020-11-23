from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField

# from crispy_forms.helper import FormHelper
# from crispy_forms.layout import Layout, Submit, Row, Column, MultiWidgetField

from datetime import datetime

from .models import User, Profile, Address


class RegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirm password', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'password')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("email is taken")
        return email

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',)

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'is_active', 'is_staff', 'is_superuser')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'mid_name', 'last_name', 'gender', 'birth_date',
                  'nationality', 'phone_number', 'pesel', 'image']

    birth_date = forms.DateField(
        required=False,
        widget=forms.SelectDateWidget(
            empty_label=("Year", "Month", "Day"),
            years=range(datetime.now().year - 120, datetime.now().year + 1)

        ))


class AddressUpdateForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['country', 'home_number', 'street', 'address', 'town', 'state', 'postal_code']

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.layout = Layout(
    #         'country',
    #         Row(
    #             Column('home_number'),
    #             Column('street'),
    #             # css_class='form-row'
    #         ),
    #         'address',
    #         Row(
    #             Column('town'),
    #             Column('state'),
    #             Column('postal_code'),
    #             # css_class='form-row'
    #         ),
    #     )
