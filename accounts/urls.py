from django.urls import path
from . import views
from rest_framework_simplejwt import views as jwt_views


urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(),
         name='token_obtain_pair'),

    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(),
         name='token_refresh'),

    path('hello/', views.HelloView.as_view(), name='hello'),

    path('register/', views.CreateUserView.as_view(), name="register"),

    path('login/', views.login, name="login"),

    path('logout/', views.logout, name="logout"),
<<<<<<< HEAD
    path('createpatient/',views.Createpatient,name="createpatient"),
    path('viewpatient/',views.PatientDetail,name="viewpatient"),
    path('cart-items/', views.CartItemViews.as_view()),
    path('cart-items/<int:id>/', views.CartItemViews.as_view()),
    path('viewproducts/',views.ProductsViewSet.as_view())
=======
>>>>>>> 7e446c4d32038da45c83a941dba267e7af264a64
]
