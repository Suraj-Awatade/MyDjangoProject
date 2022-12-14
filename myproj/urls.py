"""myproj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from myapp import views 
from allauth.account.views import confirm_email

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.hello), 
    path('index/', views.index), 
    path('show/',  views.show),
    path('index/', views.index),
    path('',include("empapp.urls")),
    path('',include("employee.urls")),
    path('',include("empinfo.urls")),
    path('auth/',include('users.urls')),
    path('blog/',include('user_blog.urls')),

]
