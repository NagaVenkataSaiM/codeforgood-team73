from django.shortcuts import render
import requests
import time



# Create your views here.
def Home(request):
	return render(request,'home.html')


def Signup(request):
	if request.POST.get('email'):
		email=request.POST.get('email')
		url='http://127.0.0.1:8000/createuser/'
		client = requests.session()
		client.get("http://127.0.0.1:8000/signup/")
		if 'csrftoken' in client.cookies:
			csrftoken = client.cookies['csrftoken']
		else:
			csrftoken = client.cookies['csrf']
		print(csrftoken)
    # Django 1.6 and up
    # older versions   
		payload={'email':email}
		r=requests.post(url,data=payload,headers={'X-CSRFToken': csrftoken},
                          allow_redirects=False)
		print(r)
	return render(request,'signup.html')