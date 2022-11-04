from django.urls import path,include
from user_blog import views
from .views import CategoriesView, CategoryWiseBlogView, BlogCountView

urlpatterns = [
  
    path('blog_registration/', views.BlogUserList.as_view()),
    path('blog_registration/<int:pk>/', views.BlogUserDetail.as_view()),
    path('categories/', CategoriesView.as_view()),
    path('categorywise_blog/',CategoryWiseBlogView.as_view()),
    path('blog_count/',BlogCountView.as_view())

]