
from django.contrib.auth import get_user_model
from rest_framework import serializers
from accounts.models import Patient

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = UserModel.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = UserModel
        # Tuple of serialized model fields (see link [2])
        fields = ("id", "username", "password", "email")

class PatientSerializer(serializers.ModelSerializer):
    profile_of=serializers.ReadOnlyField(source='user.username')
    print(profile_of)
    class Meta:
        model=Patient
        fields=['profile_of','name','gender','age','contact']
