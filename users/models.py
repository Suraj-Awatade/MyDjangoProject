# pip install django-allauth    -->>Django Allauth handles user registration as well as social authentication. It is also good for email address verification, resetting passwords and much more.
# pip install django-rest-auth  -->>Django REST Auth conveniently provides API endpoints for user registration, login/logout, password change/reset, social auth, and more.
# pip install django-rest-knox-->This is token based authintication

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import (AbstractUser, AbstractBaseUser, PermissionsMixin)
from .managers import CustomUserManager

class CustomUser(AbstractBaseUser, PermissionsMixin):
    username=None
    full_name=models.CharField(max_length=100)
    email=models.EmailField('email address',max_length=255, unique=True)
    # is_verified=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    age=models.IntegerField(null=True)
    designation=models.CharField(max_length=200,null=True,blank=True)
    contact_no=models.BigIntegerField(null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    
    objects=CustomUserManager()
    
    def __str__(self):
        return self.email
    
    def tokens(self):
        return ''
    
    
  
    
