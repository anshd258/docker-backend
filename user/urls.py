from django.urls import path
from .views import GetOTP, GetUser, CreateUser
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('get-otp/', GetOTP.as_view(), name='get-otp'),
    path('get-user/', GetUser.as_view(), name='get-user'),
    path('create-user/', csrf_exempt(CreateUser.as_view()), name='create-user'),
]
