# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import Name
from .models import Location

# Create a model serializer
class NameSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Name
        fields = ('id','first_name', 'last_name','age','email','designation','contact_no','created_at','updated_at')
        
        
        
class LocationSerializer(serializers.ModelSerializer):
    # specify model and fields
    class Meta:
        model = Location
        fields = ('id','emp_id', 'city','zip_code','landmark','street_area','description','created_at','updated_at')