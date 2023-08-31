from django.urls import path
from .views import GetOTP, GetUser, CreateUser, Checkin, Checkout
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from .views.login import Login

urlpatterns = [
    path('get-user/', GetUser.as_view(), name='get-user'),
    path('create-user/', csrf_exempt(CreateUser.as_view()), name='create-user'),
    path('checkin/', never_cache(Checkin.as_view()), name='checkin'),
    path('checkout/', never_cache(Checkout.as_view()), name='checkin'),
    path('login/', csrf_exempt(Login.as_view()), name='login'),
]
