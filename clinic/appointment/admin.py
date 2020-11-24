from django.contrib import admin

# Register your models here.
from .models import Appointment, Payment, Prescription, VisitDescription

admin.site.register(Payment)
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(VisitDescription)
