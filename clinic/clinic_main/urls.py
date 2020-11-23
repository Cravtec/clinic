from django.urls import path

from .views import about, contact, departments, FAQ, fee, index

app_name = 'clinic_main'

urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('departments/', departments, name='departments'),
    path('fees/', fee, name='fees'),
    path('FAQ/', FAQ, name='FAQ'),
]
