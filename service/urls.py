from django.urls import path
from service.views import GetMenu, CreateOrder, UpdateOrder, AddItems, FindOrders, UpdateItem, RemoveItem, GetDiscount, ApplyDiscount
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache


urlpatterns = [
    path('get-menu/', GetMenu.as_view(), name='get-menu'),
    path('create-order/', CreateOrder.as_view(), name='create-order'),
    path('add-items/', csrf_exempt(AddItems.as_view()), name='add-items'),
    path('update-order/', csrf_exempt(UpdateOrder.as_view()), name='update-order'),
    path('find-orders/', never_cache(csrf_exempt(FindOrders.as_view())), name='find-orders'),
    path('update-item/', csrf_exempt(UpdateItem.as_view()), name='update-item'),
    path('remove-item/', csrf_exempt(RemoveItem.as_view()), name='remove-item'),
    path('get-discounts/', GetDiscount.as_view(), name='get-discounts'),
    path('apply-discounts/', ApplyDiscount.as_view(), name='apply-discounts')
]
