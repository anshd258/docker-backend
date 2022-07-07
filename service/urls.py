from django.urls import path
from service.views import GetMenu, CreateOrder, UpdateOrder, AddItems, FindOrders
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('get-menu/', GetMenu.as_view(), name='get-menu'),
    path('create-order/', CreateOrder.as_view(), name='create-order'),
    path('add-items/', csrf_exempt(AddItems.as_view()), name='add-items'),
    path('update-order/', csrf_exempt(UpdateOrder.as_view()), name='update-order'),
    path('find-orders/', csrf_exempt(FindOrders.as_view()), name='find-orders')
    ]