from django.db import models
from django.contrib.auth.models import User


class Invitecodes(models.Model):
    email = models.CharField(max_length=40, null=False, blank=False)
    hashcode = models.CharField(max_length=40, null=False, blank=False)

# Models for different profiles in the app


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=40, null=False, blank=False)
