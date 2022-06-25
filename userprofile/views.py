from django.shortcuts import render
from django.http import HttpResponse
import hashlib
from .models import Invitecodes
from django.core.mail import BadHeaderError, send_mail,EmailMessage
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def Createuser(request):
	if request.POST.get('email'):
		e=request.POST.get('email')
		email_list=request.POST.get('email').split("@",2)
		email_object=hashlib.md5(email_list[0].encode())
		hcode=email_object.hexdigest()
		usermail=Invitecodes()
		usermail.email=request.POST.get('email')
		usermail.hashcode=hcode
		usermail.save()
		subject, from_email, to = 'Invitaion Link-App Name', 'from@example.com', e
		html_content='<p>Hai there,you are Invited to join </p>'+'<b>'+'App Name'+'</b>'+' Invite link: '+' <br>'+'<a href="http://appname.com/invite/'+hcode+'">'+'http://ourapp.com/invite/'+hcode+'</a>'
		email=EmailMessage(subject,html_content,to=[e])
		email.content_subtype = "html"
		email.send()
		return HttpResponse(hcode)