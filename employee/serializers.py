# import serializer from rest_framework
from rest_framework import serializers
 
# import model from models.py
from .models import Details
from .models import Address

# Create a model serializer
class DetailsSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Details
        fields = ('id','first_name', 'last_name','age','email','designation','contact_no','created_at','updated_at')
        
        
class AddressSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Address
        fields = ('emp_id', 'city','zip_code','landmark','street_area','description','created_at','updated_at')