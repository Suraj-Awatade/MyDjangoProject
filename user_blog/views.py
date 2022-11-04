from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from user_blog.models import BlogUser,Categories
from users.models import CustomUser
from rest_framework import status
from rest_framework.views import APIView
from .serializers import BlogUserSerializer, CategoriesSerializer, CategoryWiseBlogSerializer
from django.db.models import Count
from rest_framework import filters
from rest_framework import viewsets
from django.views.generic import ListView
from rest_framework import generics
from users.renderers import UserRenderer
from django.db.models import F
# from .permissions import MyPermission


# BlogUser views.
class BlogUserList(APIView):
    # permission_classes=[MyPermission]
    """
    List of all BlogUser
    
    """
    def get(self, request, format=None):
        user = BlogUser.objects.all()
        serializer = BlogUserSerializer(user, many=True)
        return Response(serializer.data)
  
    def post(self, request, format=None):
        serializer = BlogUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
  
class BlogUserDetail(APIView):
    """
    Retrieve, update or delete a blog details
    
    """
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return BlogUser.objects.get(pk=pk)
        except BlogUser.DoesNotExist:
            raise Http404
  
    def get(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = BlogUserSerializer(user)
        return Response(serializer.data)
  
    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = BlogUserSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def patch(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = BlogUserSerializer(user, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
  
    def delete(self, request, pk, format=None):
        user = BlogUser.objects.get(pk=pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Categories View  
class CategoriesView(APIView):
    
    def get(self, request, format=None):
        user = Categories.objects.all()
        serializer = CategoriesSerializer(user, many=True)
        return Response(serializer.data)
  
    def post(self, request, format=None):
        serializer = CategoriesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class CategoryWiseBlogView(APIView):
    
    def get(self, request, format=None):
        user = Categories.objects.all()
        serializer = CategoryWiseBlogSerializer(user, many=True)
        return Response(serializer.data)
    
    
class BlogCountView(APIView):
    
    #####This is one way to get auth_id,full_name and count of blogs of each author#####
    def get(self,request,format=None):
        blog_users = BlogUser.objects.all().values('auth_id').distinct()  # We get auth_id in dictinary format
        # print(blog_users)
        my_dict = []
        for item in blog_users:
            user_name= CustomUser.objects.filter(blogs__auth_id =item['auth_id']).values('full_name').annotate(auth_id = F('blogs__auth_id'), blog_count = Count('blogs__auth_id'))
            # print(user_name)
            my_dict.append(user_name[0])
               
        # print(my_dict)
        return Response(my_dict)
    
    #####This is another way to get auth_id,full_name and count of blogs of each author#####
    # def get(self,request,format=None):
    #     blog_users = BlogUser.objects.all()
    #     ids = blog_users.values('auth_id').distinct()  # We get auth_id in dictinary format
    #     # print(ids)
    #     my_dict = {}
    #     for item in ids:
    #         blog_count= BlogUser.objects.filter(auth_id=item['auth_id']).count()  
    #         user_name= CustomUser.objects.get(pk=item['auth_id']).full_name
         
    #         key=f"auth_id {item['auth_id']}"
    #         my_dict[key]={"count": blog_count,
    #                       "full_name": user_name}       
    #     # print(my_dict)
    #     return Response(my_dict)                 # no need to serialize dictinonary
