from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator

# for email account confirmation imports
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.views.generic.edit import CreateView, UpdateView

from .forms import RegistrationForm, UserCreationForm
from .models import User, Profile, Address

from django.contrib.auth.models import Group
PATIENT = Group.objects.get(name='patient')

UserModel = get_user_model()


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


def register(request):
    if request.method == 'GET':
        return render(request, 'users/register.html')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        # print(form.errors.as_data())
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            user.groups.add(PATIENT)
            Profile.objects.create(user=user)
            Address.objects.create(user=user)
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('users/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            email.send()
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


# class ProfileView(UpdateView):
#     model = User
#     fields = []
#     template_name = 'users/profile.html'
#
#     def get_success_url(self):
#         return reverse('index')
#
#     def get_object(self):
#         return self.request.user
