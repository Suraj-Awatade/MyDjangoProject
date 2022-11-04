from django.shortcuts import render

# Create your views here.
# import viewsets
from rest_framework import viewsets
 
# import local data
from .serializers import DetailsSerializer
from .serializers import AddressSerializer

from .models import Details
from .models import Address
 
# create a viewset
class DetailsViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Details.objects.all()
     
    # specify serializer to be used
    serializer_class = DetailsSerializer
    
# create a viewset
class AddressViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = Address.objects.all()
     
    # specify serializer to be used
    serializer_class = AddressSerializer


