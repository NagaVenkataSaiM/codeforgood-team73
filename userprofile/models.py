from django.db import models

# Create your models here.
class Invitecodes(models.Model):
	email=models.CharField(max_length=40,null=False,blank=False)
	hashcode=models.CharField(max_length=40,null=False,blank=False)

