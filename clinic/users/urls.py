from django.urls import path
from .views import (RegistrationView, ProfileView, profile)

from django.contrib.auth import views as auth_views

app_name = 'users'

urlpatterns = [
    path('register/', RegistrationView.as_view(template_name='users/register.html'), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/', profile, name='profile'),
]
