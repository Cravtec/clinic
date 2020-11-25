from django.db import models

# Create your models here.
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


class Payment(models.Model):
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    amount = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    status = models.BooleanField(default=False)
    appointment = models.ForeignKey(Appointment, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.appointment.profile.first_name} {self.appointment.profile.last_name} {self.amount}PLN'


class VisitDescription(models.Model):
    appointment = models.ForeignKey(Appointment, null=True, on_delete=models.DO_NOTHING)
    symptoms = models.TextField(null=True, blank=True)
    diagnose = models.TextField(null=True, blank=True)
    treatment = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.appointment.profile.first_name} {self.appointment.profile.last_name}'


class Prescription(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    date = models.DateField(auto_now_add=True, null=True, blank=True)
    appointment = models.ForeignKey(Appointment, null=True, on_delete=models.DO_NOTHING)

    def __str__(self):
        return f'{self.name} - {self.date}'
