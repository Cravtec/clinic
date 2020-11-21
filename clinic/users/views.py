from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render

from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse


from .models import User, Profile, Address
from .forms import RegistrationForm, AddressUpdateForm, ProfileUpdateForm


class RegistrationView(CreateView):
    template_name = 'users/register.html'
    form_class = RegistrationForm

    def get_context_data(self, *args, **kwargs):
        context = super(RegistrationView, self).get_context_data(*args, **kwargs)
        context['next'] = self.request.GET.get('next')
        return context

    def get_success_url(self):
        # next_url = self.request.POST.get('next')
        success_url = reverse('users:login')
        # if next_url:
        #     success_url += '?next={}'.format(next_url)
        return success_url


class ProfileView(UpdateView):
    model = User
    fields = []
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse('index')

    def get_object(self):
        return self.request.user


@login_required
def profile(request):
    if request.method == 'POST':
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        a_form = AddressUpdateForm(request.POST, instance=request.user.address)
        if p_form.is_valid() and a_form.is_valid():
            p_form.save()
            a_form.save()
            messages.success(request, f'Your profile has been updated!')
            return redirect('users:profile')
    else:
        p_form = ProfileUpdateForm(instance=request.user.profile)
        a_form = AddressUpdateForm(instance=request.user.address)
    context = {
        'p_form': p_form,
        'a_form': a_form
    }
    return render(request, 'users/profile.html', context)
