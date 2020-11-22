from django.contrib import admin
from django.contrib.auth import views as auth_views
from users import views as users_view

from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from .views import index

urlpatterns = [
    # includes
    path('users/', include('users.urls', namespace='users')),

    path('admin/', admin.site.urls),
    path('', include('clinic_main.urls', namespace='clinic_main')),
    #path('', index, name='index'),
    path('dashboard/', include('dashboard.urls', namespace='dashboard')),
    path('password_reset/',
         auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),
         name='password_reset'
         ),
    path('password_reset/done/',
         auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),
         name='password_reset_done'
         ),
    path('reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'
         ),
    path('reset-confirm/done/',
         auth_views.PasswordResetCompleteView.as_view(template_name='users/password_reset_complete.html'),
         name='password_reset_complete'
         ),
    path('password_change/',
         auth_views.PasswordChangeView.as_view(template_name='users/password_change.html'),
         name='password_change'
         ),
    path('password_change/done/',
         auth_views.PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'),
         name='password_change_done'
         ),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
