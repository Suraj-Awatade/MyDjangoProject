from django.db import models

# Create your models here.

class Name(models.Model):
    first_name=models.CharField(max_length=200)
    last_name=models.CharField(max_length=200)
    age=models.IntegerField()
    email=models.EmailField(max_length=200)
    designation=models.CharField(max_length=200)
    contact_no=models.BigIntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:  #class meta has an ordering attribute that orders the result in an ascending order based on the id.
        ordering = ('id',)   #'ordering' must be a tuple or list

    def __str__(self):
        return self.first_name
    
    
class Location(models.Model):
    emp_id=models.ForeignKey(to=Name,on_delete=models.CASCADE)
    city=models.CharField(max_length=200)
    zip_code=models.IntegerField()
    landmark=models.CharField(max_length=200)
    street_area=models.CharField(max_length=200)
    description=models.CharField(max_length=200,blank=True,null=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    
    class Meta:  #class meta has an ordering attribute that orders the result in an ascending order based on the id.
        ordering = ('emp_id',)   #'ordering' must be a tuple or list

    def __str__(self):
        return self.emp_id
    
    
    
    
    
    
    