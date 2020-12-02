from django.urls import path

from .views import *
from appointment import views as appoint_views
from django.conf.urls import url


app_name = 'dashboard'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('profile/<int:pk>/', profile, name='profile'),
    path('profile_doctor/', profile_doctor, name='profile_doctor'),
    path('profile_doctor/<int:pk>/', profile_doctor, name='profile_doctor'),
    path('doctors/', doctor, name='doctors'),
    path('patients/', patient, name='patients'),
    path('appointments/', appointment, name='appointments'),
    path('update_appointment/<int:pk>/',
         appoint_views.AppointmentUpdateView.as_view(),
         name='update_appointment'
         ),
    path('delete_confirm_appointment/<int:pk>/',
         appoint_views.AppointmentDeleteView.as_view(),
         name='delete_confirm_appointment'
         ),
    path('calendar/', CreateAppointmentView.as_view(), name='calendar'),
    url('calendar/hours/', check_hours, name='check_hours'),
    path('medical_history/', medical_history, name='medical_history'),
    path('create_patient/', register_patient, name='create_patient'),
    path('create_doctor/', register_doctor, name='create_doctor'),
    path('create_secretary/', register_secretary, name='create_secretary'),

]

# path('<int:pk>/update_profile/', ProfileUpdateView.as_view(), name='update_profile'),
# path('<int:pk>/update_doctor/', DoctorUpdateView.as_view(), name='update_doctor'),
# path('<int:pk>/update_address/', AddressUpdateView.as_view(), name='update_address'),
#     path('profile_edit/', profile_edit, name='profile_edit'),
#     path('doctors/', doctor, name='doctor'),
#     path('appointments/', appointment, name='appointment'),
#     path('calendar/', CreateAppointmentView.as_view(), name='calendar'),
#     path('medical_history/', medical_history, name='medical_history'),
# # ]
