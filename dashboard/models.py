from django.db import models
from userprofile.models import Doctor
from accounts.models import Patient


class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True)
    meeting_preference = models.CharField(max_length=8, null=True, blank=True)
    purpose = models.TextField(max_length=512, null=True, blank=True)
