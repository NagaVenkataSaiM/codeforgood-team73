from django.shortcuts import render
import requests
import time
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status

from dashboard.models import Appointment
from .serializers import AppointmentSerializer


# Create your views here.
def Home(request):
    return render(request, 'home.html')


def Signup(request):
    if request.POST.get('email'):
        email = request.POST.get('email')
        url = 'http://127.0.0.1:8000/createuser/'
        client = requests.session()
        client.get("http://127.0.0.1:8000/signup/")
        if 'csrftoken' in client.cookies:
            csrftoken = client.cookies['csrftoken']
        else:
            csrftoken = client.cookies['csrf']
        print(csrftoken)
    # Django 1.6 and up
    # older versions
        payload = {'email': email}
        r = requests.post(url, data=payload, headers={'X-CSRFToken': csrftoken},
                          allow_redirects=False)
        print(r)
    return render(request, 'signup.html')


@api_view(['POST'])
@permission_classes((permissions.IsAuthenticated))
def create_appointment(request):
    if request.user.is_staff:
        try:
            patient = request.POST.get('patient')
            doctor = request.POST.get('doctor')
            date = request.POST.get('date')
            time = request.POST.get('time')
            status = request.POST.get('status')
            meeting_preference = request.POST.get('meeting_preference')
            purpose = request.POST.get('purpose')
            Appointment.object.create(patient=patient, doctor=doctor, date=date, time=time, status=status,
                                      meeting_preference=meeting_preference, purpose=purpose)
            return Response(status=status.HTTP_200_OK)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("You are not authorized to create an appointment", status=status.HTTP_401_UNAUTHORIZED)


@api_view(['GET'])
@permission_classes((permissions.IsAuthenticated))
def get_appointments(request):
    if request.user.is_staff:
        try:
            appointments = Appointment.object.all()
            serializer = AppointmentSerializer(appointments, many=True)
            return Response(serializer.data)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response("You are not authorized to get appointments", status=status.HTTP_401_UNAUTHORIZED)
