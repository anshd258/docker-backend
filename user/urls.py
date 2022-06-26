from django.urls import path
from .views import GetOTP, GetUser, CreateUser


urlpatterns = [
    path('get-otp/', GetOTP.as_view(), name='get-otp'),
    path('get-user/', GetUser.as_view(), name='get-user'),
    path('create-user/', CreateUser.as_view(), name='create-user'),
]
