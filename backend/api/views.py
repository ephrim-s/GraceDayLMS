import random
from django.shortcuts import render
from api import srializers as api_serializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from userauths.models import User, Profile


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = api_serializer.MyTokenObtainPairSerializer

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_class = [AllowAny]
    serializer_class = api_serializer.RegisterSerializer

def generate_random_otp(length=6):
    otp = "".join([str(random.randint(0, 9)) for _ in range(length)])
    return otp

class PasswordResetEmailVerifyAPIView(generics.RetrieveAPIView):
   permission_class = [AllowAny]
   serializer_class = api_serializer.UserSerializer

   def get_object(self):
       email = self.kwargs['email'] #api/v1/password-email-verify/amdmin@example.com
       user = User.objects.filter(email=email).first()

       if user:
           uuidb64 = user.pk
           refresh = RefreshToken.for_user(user)
           refresh_token = str(refresh.access_token)
           user.refresh_token = refresh_token
           user.otp = generate_random_otp()
           user.save()
           link = f"http://localhost:5173/create-new-password/?otp={user.otp}&uuidb64={uuidb64}&=refresh_token={refresh_token}"
           print("link ========", link)

       return user
   
class PasswordChandeAPIView(generics.CreateAPIView):
    permission_class = [AllowAny]
    serializer_class = api_serializer.UserSerializer

    def create(self, request, *args, **kwargs):
        otp = request.data['otp']
        uuidb64 = request.data['uuidb64']
        password = request.data['password']

        user = User.objects.get(id=uuidb64, otp=otp)
        if user:
            user.set_password(password)
            user.otp = ""
            user.save()

            return Response({"message":"Password Changed Successfully"}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message":"User Does not Exits"}, status=status.HTTP_404_NOT_FOUND)