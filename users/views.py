from django.shortcuts import render
from rest_framework import generics,status,permissions
from rest_framework.response import Response
from .models import CustomUser
from rest_framework import status
from rest_framework.views import APIView
from .serializers import (RegisterSerializer, UserLoginSerializer, SendPasswordResetEmailSerializer,
                          UserPasswordResetSerializer, CustomUserSerializer, UserWiseBlogSerializer)
from knox.models import AuthToken
from django.contrib.auth import authenticate
from .renderers import UserRenderer
# from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


# class RegisterView(generics.GenericAPIView):
#     serializer_class=RegisterSerializer
#     renderer_classes = [UserRenderer]

    # def post(self, request, *args, **kwargs):
    #     serializer = self.get_serializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     user = serializer.save()
    #     @receiver(post_save, sender=settings.AUTH_USER_MODEL)
    #     def create_auth_token(sender, instance=None, created=False, **kwargs):
    #         if created:
    #             Token.objects.create(user=instance)
        
    #     return Response({
    #     "user": RegisterSerializer(user, context=self.get_serializer_context()).data,
    #     "token": Token.objects.create(user)
    #     })

class GetUserView(APIView):
    """
    List of all Users
    
    """
    def get(self, request, format=None):
        user = CustomUser.objects.all()
        serializer = CustomUserSerializer(user, many=True)
        return Response(serializer.data)
    

class GetUserWiseBlogView(APIView):
    """
    List of all User Wise Blogs
    
    """
    def get(self, request, format=None):
        user = CustomUser.objects.all()
        serializer = UserWiseBlogSerializer(user, many=True)
        return Response(serializer.data)
    
class RegisterView(generics.GenericAPIView):
    
        def get(self,request):
            return Response({'msg':'Get Request'})
        
        def post(self,request):
            serializer = RegisterSerializer(data=request.data)
            data = {}
            if serializer.is_valid():
                user = serializer.save()
                data['response'] = "Successfully Registered a new user"
                data['full_name'] = user.full_name
                # data['age'] = user.age
                # data['designation'] = user.designation
                # data['contact_no'] = user.contact_no
                data['email'] = user.email
                token = Token.objects.get(user=user).key
                data['token'] = token
            else:
                data = serializer.errors
            return Response(data)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
        
# class UserLoginView(generics.GenericAPIView):
#   renderer_classes = [UserRenderer]
#   def post(self, request, format=None):
#     serializer = UserLoginSerializer(data=request.data)
#     serializer.is_valid(raise_exception=True)
#     email = serializer.data.get('email')
#     password = serializer.data.get('password')
#     user = authenticate(email=email, password=password)
#     if user is not None:
#         token = Token.objects.get_or_create(user=user)
#         # token = get_tokens_for_user(user)
#         return Response({'token':token, 'msg':'Login Success'}, status=status.HTTP_200_OK)
#     else:
#       return Response({'errors':{'non_field_errors':['Email or Password is not Valid']}}, status=status.HTTP_404_NOT_FOUND)
    

class SendPasswordResetEmailView(generics.GenericAPIView):
  renderer_classes = [UserRenderer]
  def post(self, request, format=None):
    serializer = SendPasswordResetEmailSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        return Response({'msg':'Password Reset link send. Please check your Email'}, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserPasswordResetView(generics.GenericAPIView):
  renderer_classes = [UserRenderer]
  def post(self, request, uid, token, format=None):
    serializer = UserPasswordResetSerializer(data=request.data, context={'uid':uid, 'token':token})
    if serializer.is_valid(raise_exception=True):
        return Response({'msg':'Password Reset Successfully'}, status=status.HTTP_200_OK)  
        
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# from rest_framework.authtoken.models import Token
# for user in CustomUser.objects.all():    #creating tokens for users if user is already registered.
#     Token.objects.get_or_create(user=user)





