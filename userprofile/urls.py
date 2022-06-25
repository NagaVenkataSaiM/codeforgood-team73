from django.urls import path, include
# now import the views.py file into this code
from . import views

urlpatterns = [
    # path('createuser/',views.Createuser,name='createuser'),
    path('doctors/', views.getDoctors),
    path('create-doctor/', views.createDoctor),
    path('update-doctor/', views.updateDoctor),
    path('get-doctor/', views.getDoctor),
]
