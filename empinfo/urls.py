
# # basic URL Configurations
# from django.urls import include, path
# # import routers
# from rest_framework import routers
 
# # import everything from views
# from .views import *
 
# # define the router
# router = routers.DefaultRouter()
 
# # define the router path and viewset to be used
# router.register(r'details', DetailsViewSet)
# router.register(r'address', AddressViewSet)

# # specify URL Path for rest_framework
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls'))
# ]


from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from empinfo import views
  
urlpatterns = [
    path('name/', views.NameList.as_view()),
    path('name/<int:pk>/', views.NameDetail.as_view()),
    path('location/', views.LocationList.as_view()),
    path('location/<int:pk>/', views.LocationDetail.as_view()),
]
  
urlpatterns = format_suffix_patterns(urlpatterns)
