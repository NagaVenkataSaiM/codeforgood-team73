from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from .serializers import UserSerializer,PatientSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework import generics
# for testing the hello world api endpoint
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from accounts.models import Patient


class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    """
    POST accounts/login/
    """
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=status.HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def logout(request):
    """
    POST accounts/logout/
    """
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)

class CreatePatient(generics.ListCreateAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

    def perform_create(self, serializer):
        serializer.save(profile_of=self.request.user)

class PatientDetail(generics.RetrieveAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

# @csrf_exempt
# @api_view(["POST"])
# @permission_classes((IsAuthenticated,))
# def Createpatient(request):
#     profile_of=request.user
#     name=request.POST.get('name')
#     gender=request.POST.get('gender')
#     age=request.POST.get('age')
#     contact=request.POST.get('contact')
#     try:
#         Patient.objects.create(profile_of=profile_of,name=name,gender=gender,age=age,contact=contact)
#         return Response(status=status.HTTP_200_OK)
#     except:
#         return Response(status=status.HTTP_400_BAD_REQUEST)





