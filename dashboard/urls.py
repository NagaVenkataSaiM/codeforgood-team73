from django.urls import path,include
#now import the views.py file into this code
from . import views

urlpatterns=[
	path('',views.Home,name='home'),
	path('signup/',views.Signup,name='signup')

]