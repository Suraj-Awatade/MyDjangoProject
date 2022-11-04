from django.contrib import admin
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from user_blog.models import BlogUser, Categories

admin.site.register(BlogUser)
admin.site.register(Categories)