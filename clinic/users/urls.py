from django.contrib.auth import views as auth_views
from django.urls import path

from .views import register, activate

app_name = 'users'

urlpatterns = [
    path('register/', register, name="register"),
    path('activate/<uidb64>/<token>/', activate, name='activate'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

]
