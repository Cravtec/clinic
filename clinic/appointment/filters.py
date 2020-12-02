import django_filters
from django_filters import CharFilter, DateFilter

from .models import *


class AppointmentFilter(django_filters.FilterSet):
    date = DateFilter(label='Date', field_name='date', lookup_expr='gte')

    class Meta:
        model = Appointment
        fields = ['date', 'profile', 'doctor']
