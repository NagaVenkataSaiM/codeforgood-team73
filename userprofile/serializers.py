from pydoc import Doc
from statistics import mode
from telnetlib import DO
from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta :
        model = Doctor
        fields = '__all__'