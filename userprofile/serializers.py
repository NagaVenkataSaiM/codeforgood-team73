from pydoc import Doc
from statistics import mode
from telnetlib import DO
from rest_framework import serializers
from .models import Doctor
from django.contrib.auth.models import User


class DoctorSerializer(serializers.ModelSerializer):

    user = serializers.PrimaryKeyRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=User.objects.all(),
    )

    class Meta:
        model = Doctor
        fields = ['name', 'user', 'email', 'phone',
                  'specialization', 'city', 'gender']
