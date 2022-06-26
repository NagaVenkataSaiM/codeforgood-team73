from django.urls import path, include
# now import the views.py file into this code
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('signup/', views.Signup, name='signup'),

    path('create-appointment/', views.create_appointment),

    path('get-appointments/', views.get_appointments),

    path('create-usercounselling/', views.create_usercounselling),

    path('update-usercounselling-status', views.update_usercounselling_status),

    path('get-usercounselling', views.get_usercounselling)
]
