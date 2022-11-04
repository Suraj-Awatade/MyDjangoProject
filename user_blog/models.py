from django.db import models

# Create your models here.
class BlogUser(models.Model):
    auth_id = models.ForeignKey("users.CustomUser", verbose_name=("AUTH_ID"), on_delete=models.CASCADE, 
                                db_column='auth_id', related_name='blogs')
    blog_title=models.CharField(max_length=200)
    email=models.EmailField(max_length=200)
    description=models.CharField(max_length=500,null=True)
    created_on=models.DateTimeField(auto_now_add=True)
    updated_on=models.DateTimeField(auto_now=True)
    category_id=models.ForeignKey("user_blog.Categories", on_delete=models.CASCADE,
                                  db_column='category_id', related_name='categories')
    
    
    def __str__(self):
        return self.auth_id
    

class Categories(models.Model):
    category_name=models.CharField(max_length=50)
    
    def __str__(self):
        return self.category_name
    
        