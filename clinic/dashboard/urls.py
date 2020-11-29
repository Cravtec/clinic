from django.urls import path

from .views import (dashboard, profile_edit, doctor, appointment, calendar, profile, medical_history, register_patient,
                    register_doctor, register_secretary)

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('<int:PK>/profile/', profile, name='profile'),
    path('profile_edit/', profile_edit, name='profile_edit'),
    path('doctors/', doctor, name='doctor'),
    path('appointments/', appointment, name='appointment'),
    path('calendar/', calendar, name='calendar'),
    path('medical_history/', medical_history, name='medical_history'),
    path('create_patient/', register_patient, name='create_patient'),
    path('create_doctor/', register_doctor, name='create_doctor'),
    path('create_secretary/', register_secretary, name='create_secretary'),
]
