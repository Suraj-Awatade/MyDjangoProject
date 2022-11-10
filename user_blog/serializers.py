from rest_framework import serializers
from .models import BlogUser, Categories
from rest_framework.validators import UniqueTogetherValidator
from django.db.models import Count

class BlogUserSerializer(serializers.ModelSerializer):
  class Meta:
    model=BlogUser
    fields=['id','auth_id','email','blog_title', 'category_id','description','created_on','updated_on']
    
          
class CategoriesSerializer(serializers.ModelSerializer):
  class Meta:
      model=Categories
      fields=['id','category_name']
      validators = [                                # This makes unique constraint to category_name column
            UniqueTogetherValidator(
                queryset=Categories.objects.all(),
                fields=['category_name',]
            )
        ]
      
      
class CategoryWiseBlogSerializer(serializers.ModelSerializer):
  catergorywise_blog_list = serializers.SerializerMethodField()
  def get_catergorywise_blog_list(self,obj):
     user_category = obj.categories.all()     #blogs is related name of bloguser model.
     serializer = BlogUserSerializer(user_category,many=True)
     return serializer.data
  class Meta:
      model=Categories
      fields=['id','category_name','catergorywise_blog_list']
      validators = [                                # This makes unique constraint to category_name column
            UniqueTogetherValidator(
                queryset=Categories.objects.all(),
                fields=['category_name',]
            )
        ]  
