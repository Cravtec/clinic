from django.db import models

# Create your models here.
from django.urls import reverse
from users import models as user_models


class Appointment(models.Model):
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    end_time = models.TimeField(auto_now=False, auto_now_add=False, null=True, blank=True)
    profile = models.ForeignKey(user_models.Profile, null=True, on_delete=models.DO_NOTHING)
    doctor = models.ForeignKey(user_models.Doctor, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.date}: {self.profile.first_name} {self.profile.last_name} | ' \
               f'Dr({self.doctor.first_name} {self.doctor.last_name})'

    @property
    def get_html_url(self):
        url = reverse('event_edit', args=(self.id,))
        return f'<p>{self.id}</p><a href="{url}">edit</a>'


class Payment(models.Model):
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    status = models.BooleanField(default=False)
    appointment = models.ForeignKey(Appointment, null=True, on_delete=models.CASCADE, related_name='payment')

    def __str__(self):
        return f'{self.appointment.profile.first_name} {self.appointment.profile.last_name} {self.amount}PLN'


class VisitDescription(models.Model):
    appointment = models.ForeignKey(Appointment, null=True, on_delete=models.CASCADE, related_name='visit')
    symptoms = models.TextField(null=True, blank=True)
    diagnose = models.TextField(null=True, blank=True)
    treatment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.appointment.profile.first_name} {self.appointment.profile.last_name}'


class Prescription(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    appointment = models.ForeignKey(Appointment, null=True, on_delete=models.CASCADE, related_name='prescription')

    def __str__(self):
        return f'{self.name} - {self.date}'

class Event(models.Model):
    def current_app(self, doctor_id, current_date):
        return self.filter()