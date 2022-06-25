from django.urls import path,include
#now import the views.py file into this code
from . import views

urlpatterns=[
	# path('createuser/',views.Createuser,name='createuser'),
	path('doctors/',views.getDoctors),
	path('create-doctor/',views.CreateDoctorView.as_view())
]