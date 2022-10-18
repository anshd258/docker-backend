from django.urls import path
from .views import GetOTP, GetUser, CreateUser, Checkin
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache


urlpatterns = [
    path('get-otp/', GetOTP.as_view(), name='get-otp'),
    path('get-user/', GetUser.as_view(), name='get-user'),
    path('create-user/', csrf_exempt(CreateUser.as_view()), name='create-user'),
    path('checkin/', never_cache(Checkin.as_view()), name='checkin')
]
