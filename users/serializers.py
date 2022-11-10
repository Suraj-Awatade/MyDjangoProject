from rest_framework import serializers
from .models import CustomUser
from django.utils.encoding import smart_str, force_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from .utils import Util
from user_blog.serializers import BlogUserSerializer


# class RegisterSerializer(serializers.ModelSerializer):
#     password=serializers.CharField(max_length=68,
#                                    min_length=6, write_only=True)
    

#     class Meta:
#         model = CustomUser
#         fields = ['email', 'password', 'token']
        
#     def validate(self,attrs):   
#         email=attrs.get('email','')
#         password=attrs.get('password','')
#         token=attrs.get('token','')
        
#         if not password.isalnum():
#             raise serializers.ValidationError('The Password should only contain alphanumeric characters')
#         return attrs
    
    
class CustomUserSerializer(serializers.ModelSerializer):
  
  class Meta:
      model=CustomUser
      fields=['id','full_name','email','age','designation','contact_no','created_at','updated_at']


class UserWiseBlogSerializer(serializers.ModelSerializer):
  user_list = serializers.SerializerMethodField()
  def get_user_list(self,obj):
     blog_user = obj.blogs.all()     #blogs is related name of bloguser model.
     serializer = BlogUserSerializer(blog_user,many=True)
     return serializer.data
  class Meta:
      model=CustomUser
      fields=['id','full_name','email','age','designation','contact_no','created_at','updated_at','user_list']
      
      
class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)
    class Meta:
        model = CustomUser
        fields = ["full_name","email","password","password2","age","designation","contact_no"]
        extra_kwargs = {'password':{'write_only': True}}
        
    def save(self):
        user = CustomUser(
            email=self.validated_data['email'],
            full_name=self.validated_data['full_name'],
            age=self.validated_data['age'],
            designation=self.validated_data['designation'],
            contact_no=self.validated_data['contact_no'],
            # is_admin = self.validated_data['is_admin'],
            # is_staff = self.validated_data['is_staff']
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password': 'Passwords must match.'})
        user.set_password(password)
        user.save()
        return user
    
    
# class UserLoginSerializer(serializers.ModelSerializer):
#   email = serializers.EmailField(max_length=255)
#   class Meta:
#     model = CustomUser
#     fields = ['email', 'password']
    
    
class SendPasswordResetEmailSerializer(serializers.ModelSerializer):
  email = serializers.EmailField(max_length=255)
  class Meta:
      model=CustomUser
      fields = ['email']

  def validate(self, attrs):
    email = attrs.get('email')
    if CustomUser.objects.filter(email=email).exists():
      user = CustomUser.objects.get(email = email)
      uid = urlsafe_base64_encode(force_bytes(user.id))
      # print('Encoded UID', uid)
      token = PasswordResetTokenGenerator().make_token(user)
      # print('Password Reset Token', token)
      link = 'http://localhost:8000/api/user/reset/'+uid+'/'+token
      # print('Password Reset Link', link)
      # Send EMail
      body = 'Click Following Link to Reset Your Password '+link
      data = {
        'subject':'Reset Your Password',
        'body':body,
        'to_email':user.email
      }
      Util.send_email(data)
      return attrs
    else:
      raise serializers.ValidationError('You are not a Registered User')

    
class UserPasswordResetSerializer(serializers.Serializer):
  password = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  password2 = serializers.CharField(max_length=255, style={'input_type':'password'}, write_only=True)
  class Meta:
      model=CustomUser
      fields = ['password', 'password2']

  def validate(self, attrs):
    try:
      password = attrs.get('password')
      password2 = attrs.get('password2')
      uid = self.context.get('uid')
      token = self.context.get('token')
      if password != password2:
        raise serializers.ValidationError("Password and Confirm Password doesn't match")
      id = smart_str(urlsafe_base64_decode(uid))
      user = CustomUser.objects.get(id=id)
      if not PasswordResetTokenGenerator().check_token(user, token):
        raise serializers.ValidationError('Token is not Valid or Expired')
      user.set_password(password)
      user.save()
      return attrs
    except DjangoUnicodeDecodeError as identifier:
      PasswordResetTokenGenerator().check_token(user, token)
      raise serializers.ValidationError('Token is not Valid or Expired')

