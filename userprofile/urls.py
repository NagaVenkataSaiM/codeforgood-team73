from django.urls import path,include
#now import the views.py file into this code
from . import views

urlpatterns=[
	path('createuser/',views.Createuser,name='createuser')

]