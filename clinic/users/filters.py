import django_filters
from django_filters import CharFilter

from .models import *


class ProfileFilter(django_filters.FilterSet):
    first_name = CharFilter(label='First name', field_name='first_name', lookup_expr='icontains')
    last_name = CharFilter(label='Last name', field_name='last_name', lookup_expr='icontains')
    pesel = CharFilter(label='PESEL', field_name='pesel', lookup_expr='icontains')

    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'pesel', 'gender']


class DoctorFilter(django_filters.FilterSet):
    first_name = CharFilter(label='First name', field_name='first_name', lookup_expr='icontains')
    last_name = CharFilter(label='Last name', field_name='last_name', lookup_expr='icontains')

    class Meta:
        model = Doctor
        fields = ['first_name', 'last_name', 'specialization', 'phone_number']
