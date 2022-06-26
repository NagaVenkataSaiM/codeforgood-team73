from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.generics import CreateAPIView

from .serializers import UserSerializer,PatientSerializer,CartItemSerializer,ProductSerializer

from .serializers import UserSerializer

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework import generics
# for testing the hello world api endpoint
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from accounts.models import Patient,CartItem,Product



class CreateUserView(CreateAPIView):

    model = get_user_model()
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]
    serializer_class = UserSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    """
    POST accounts/login/
    """
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=status.HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=status.HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def logout(request):
    """
    POST accounts/logout/
    """
    request.user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)


# class CreatePatient(generics.ListCreateAPIView):
#     queryset = Patient.objects.all()
#     serializer_class = PatientSerializer

#     def perform_create(self, serializer):
#         serializer.save(profile_of=self.request.user)
@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def PatientDetail(request):
    queryset = Patient.objects.get(profile_of=request.user)
    serializer_class = PatientSerializer(queryset)
    return Response(serializer_class.data)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def Createpatient(request):
    profile_of=request.user
    name=request.POST.get('name')
    gender=request.POST.get('gender')
    age=request.POST.get('age')
    contact=request.POST.get('contact')
    try:
        Patient.objects.create(profile_of=profile_of,name=name,gender=gender,age=age,contact=contact)

        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

class CartItemViews(APIView):
    def post(self, request):
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
        else:
            return Response({"status": "error", "data": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request, id=None):
        if id:
            item = CartItem.objects.get(id=id)
            serializer = CartItemSerializer(item)
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)

        items = CartItem.objects.all()
        serializer = CartItemSerializer(items, many=True)
        return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
    def patch(self, request, id=None):
        item = CartItem.objects.get(id=id)
        serializer = CartItemSerializer(item, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data})
        else:
            return Response({"status": "error", "data": serializer.errors})

    def delete(self, request, id=None):
        item = get_object_or_404(CartItem, id=id)
        item.delete()
        return Response({"status": "success", "data": "Item Deleted"})

def AllItems(request):
    x=CartItem.objects.get(cart_owner=request.user)
    serializer_class = CartItemSerializer(x)
    return Response(serializer_class.data)


class ProductsViewSet(generics.ListCreateAPIView):
    """List products viewset"""

    def list(self, request):
        queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data)

@csrf_exempt
@api_view(["POST"])
@permission_classes((IsAuthenticated,))
def createProduct(request):
    name=request.POST.get('name')
    description=request.POST.get('description')
    image=request.POST.get('image')
    price=request.POST.get('price')
    try:
        Product.objects.create(name=name,description=description,image=image,price=price)
        return Response(status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)


