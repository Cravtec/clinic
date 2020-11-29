
from django.urls import path


from .views import dashboard, profile_edit, doctor, appointment, calendar, profile, app_cal, check_hours

app_name = 'dashboard'

urlpatterns = [
    path('', dashboard, name='dashboard'),
    path('profile/', profile, name='profile'),
    path('profile_edit/', profile_edit, name='profile_edit'),
    path('doctors/', doctor, name='doctor'),
    path('appointments/', appointment, name='appointment'),
    path('calendar/', calendar, name='calendar'),
    path('medical_history/', app_cal, name='medical_history'),
    path('app_cal/', app_cal, name='app_cal'),
    path('calendar/hours/', check_hours, name='check_hours'),
    # path('myajaxtest/', views.myajaxtestview, name='ajax-test-view'),
]
