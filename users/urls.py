from django.urls import path,include
from .views import RegisterView, SendPasswordResetEmailView, UserPasswordResetView, GetUserView, GetUserWiseBlogView
from rest_framework.authtoken import views


urlpatterns = [
    path('getuser/', GetUserView.as_view(), name="getuser"),
    path('register/', RegisterView.as_view(), name="register"),
    path('login/', views.obtain_auth_token, name="login"),    #login view is imported from rest_framework.authtoken views.
    path('send-reset-password-email/', SendPasswordResetEmailView.as_view(), name='send-reset-password-email'),
    path('reset-password/<uid>/<token>/', UserPasswordResetView.as_view(), name='reset-password'),
    path('getuserwiseblog/',GetUserWiseBlogView.as_view(),name="getuserwiseblog")
]
