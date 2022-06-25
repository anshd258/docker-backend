from django.urls import path
from service.views import GetMenu, CreateOrder, UpdateOrder

urlpatterns = [
    path('get-menu/', GetMenu.as_view(), name='get-menu'),
    path('create-order/', CreateOrder.as_view(), name='create-order'),
    path('update-order/', UpdateOrder.as_view(), name='update-order')
    ]
