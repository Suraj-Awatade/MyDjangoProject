from django.shortcuts import render
from django.http import Http404
  
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
  
from empinfo.models import Name
from empinfo.serializers import NameSerializer
from empinfo.models import Location
from empinfo.serializers import LocationSerializer
  
class NameList(APIView):
    """
    List of all Employees
    
    """
  
    def get(self, request, format=None):
        name = Name.objects.all()
        serializer = NameSerializer(name, many=True)
        return Response(serializer.data)
  
    def post(self, request, format=None):
        serializer = NameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
class NameDetail(APIView):
    """
    Retrieve, update or delete a employee details
    
    """
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Name.objects.get(pk=pk)
        except Name.DoesNotExist:
            raise Http404
  
    def get(self, request, pk, format=None):
        name = self.get_object(pk)
        serializer = NameSerializer(name)
        return Response(serializer.data)
  
    def put(self, request, pk, format=None):
        name = self.get_object(pk)
        serializer = NameSerializer(name, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def patch(self, request, pk, format=None):
        name = self.get_object(pk)
        serializer = NameSerializer(name, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
  
    def delete(self, request, pk, format=None):
        name = Name.objects.get(pk=pk)
        name.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    
class LocationList(APIView):
    """
    Location/Address details of all Employees
    """
  
    def get(self, request, format=None):
        location = Location.objects.all()
        serializer = LocationSerializer(location, many=True)
        return Response(serializer.data)
  
    def post(self, request, format=None):
        serializer = LocationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


class LocationDetail(APIView):
    """
    Retrieve, update or delete a employee instance
    """
    def get_object(self, pk):
        # Returns an object instance that should 
        # be used for detail views.
        try:
            return Location.objects.get(pk=pk)
        except Location.DoesNotExist:
            raise Http404
  
    def get(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location)
        return Response(serializer.data)
  
    def put(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  
    def patch(self, request, pk, format=None):
        location = self.get_object(pk)
        serializer = LocationSerializer(location, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
          
  
    def delete(self, request, pk, format=None):
        location = Location.objects.get(pk=pk)
        location.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
