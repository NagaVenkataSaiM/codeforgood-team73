from os import stat
from django.shortcuts import render
from django.http import HttpResponse
import hashlib
from .models import Invitecodes
from django.core.mail import BadHeaderError, send_mail, EmailMessage
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from .serializers import DoctorSerializer
from .models import Doctor
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView


@csrf_exempt
def Createuser(request):
    if request.POST.get('email'):
        e = request.POST.get('email')
        email_list = request.POST.get('email').split("@", 2)
        email_object = hashlib.md5(email_list[0].encode())
        hcode = email_object.hexdigest()
        usermail = Invitecodes()
        usermail.email = request.POST.get('email')
        usermail.hashcode = hcode
        usermail.save()
        subject, from_email, to = 'Invitaion Link-App Name', 'from@example.com', e
        html_content = '<p>Hai there,you are Invited to join </p>'+'<b>'+'App Name'+'</b>'+' Invite link: ' + \
            ' <br>'+'<a href="http://appname.com/invite/'+hcode + \
            '">'+'http://ourapp.com/invite/'+hcode+'</a>'
        email = EmailMessage(subject, html_content, to=[e])
        email.content_subtype = "html"
        email.send()
        return HttpResponse(hcode)


# # Views for the profiles of users

# @api_view['POST']
# def Update_doctor_profile(request):
@api_view(['GET'])  
# @permission_classes((permissions.AllowAny))
def getDoctors(request):

    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(doctors,many=True)
    return Response(serializer.data)

# class CreateDoctorView(CreateAPIView):

#     model = Doctor
#     permission_classes = [
#         permissions.IsAuthenticated   # Or anon users can't register
#     ]
#     serializer_class = DoctorSerializer

@api_view(['POST'])
# @permission_classes((permissions.IsAuthenticated))
def createDoctor(request):
    try:
        name = request.POST.get('name')
        user = request.user
        email = request.user.email
        phone = request.POST.get('phone')
        specialization = request.POST.get('specialization')
        city = request.POST.get('city')
        gender = request.POST.get('gender')

        
        Doctor.objects.create(name=name,user=user,email=email,phone=phone,specialization=specialization,city=city,gender=gender)

        return Response('Created',status=status.HTTP_201_CREATED)
    except:
        return Response('Failed',status=status.HTTP_400_BAD_REQUEST)