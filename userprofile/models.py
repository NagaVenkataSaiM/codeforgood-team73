from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator,MaxValueValidator

class Invitecodes(models.Model):
    email = models.CharField(max_length=40, null=False, blank=False)
    hashcode = models.CharField(max_length=40, null=False, blank=False)

# Models for different profiles in the app


class Doctor(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,default=1,primary_key=True)
    email = models.CharField(max_length=100,null=True,blank=True)
    phone = models.IntegerField(null=True,blank=True,validators=[MinValueValidator(1000000000),MaxValueValidator(9999999999)])
    specialization = models.CharField(max_length=255,null=True, blank=True)
    city = models.CharField(max_length=255,null=True,blank=True)
    gender = models.CharField(max_length=1,null=True,blank=True)    
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
