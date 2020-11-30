from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse, resolve
from django.test import SimpleTestCase

from users.views import register, activate


class TestUrls(SimpleTestCase):

    def test_register_url(self):
        url = reverse('users:register')
        self.assertEquals(resolve(url).func, register)

    def test_activate_url(self):
        url = reverse('users:activate', args=['some-slug', 'some-slug'])
        self.assertEquals(resolve(url).func, activate)

    def test_login_url(self):
        url = reverse('users:login')
        self.assertEquals(resolve(url).func.view_class, LoginView)

    def test_logout_url(self):
        url = reverse('users:logout')
        self.assertEquals(resolve(url).func.view_class, LogoutView)


