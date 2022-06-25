from django.db import models


# Create your models here.
class Patient(models.Model):
		profile_of = models.CharField(max_length=100, blank=True, default='')
		name=models.CharField(max_length=100, blank=True, default='')
		gender=models.CharField(max_length=10, blank=True, default='')
		age = models.IntegerField()
		contact=models.BigIntegerField()