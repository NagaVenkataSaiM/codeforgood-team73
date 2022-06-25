from rest_framework import serializers
from .models import Appointment, UserCounselling


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = '__all__'


class UserCounsellingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCounselling
        fields = '__all__'
