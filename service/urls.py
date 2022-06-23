from django.urls import path
from service.views import GetMenu

urlpatterns = [
    path('get-menu/', GetMenu.as_view(), name='get-menu'),
    ]
