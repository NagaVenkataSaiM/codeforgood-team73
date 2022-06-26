from django.db import models
from userprofile.models import Doctor
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class UserCounselling(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=True, blank=True)
    gender = models.CharField(max_length=2, null=True, blank=True)
    age = models.IntegerField(default=0, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)

    problem = models.CharField(max_length=512, null=True, blank=True)
    contact_number = models.IntegerField(null=True, blank=True, validators=[
                                         MinValueValidator(1000000000), MaxValueValidator(9999999999)])
    is_assigned = models.BooleanField(default=False)


class Appointment(models.Model):
    patient = models.ForeignKey(UserCounselling, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    status = models.CharField(max_length=10, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True)
    meeting_preference = models.CharField(max_length=8, null=True, blank=True)
    purpose = models.TextField(max_length=512, null=True, blank=True)
