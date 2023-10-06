from django.urls import path
from service.views import *
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache

urlpatterns = [
    path('get-all-foods/', never_cache(GetMenu.as_view()), name='get-menu'),
    path('create-foodorder/', CreateOrder.as_view(), name='create-order'),
    path('add-fooditems/', csrf_exempt(AddItems.as_view()), name='add-items'),
    path('update-foodorder/', csrf_exempt(UpdateOrder.as_view()), name='update-order'),
    path('find-foodorder/', never_cache(csrf_exempt(FindOrder.as_view())), name='find-orders'),
    path('update-foodorderitem/', csrf_exempt(UpdateItem.as_view()), name='update-item'),
    path('remove-fooditems/', csrf_exempt(RemoveItem.as_view()), name='remove-item'),
    path('get-discounts/', GetDiscount.as_view(), name='get-discounts'),
    path('apply-discounts/', ApplyDiscount.as_view(), name='apply-discounts'),
    path('get-order-by-type/',GetOrderByType, name='get-order-by-type'),
    path('create-rentalbooking/', csrf_exempt(CreateRentalBooking), name='create-rentalbooking'),
    path('create-ride/', csrf_exempt(CreateRide), name='create-ride'),
    path('set-status-rental/', csrf_exempt(SetStatusRental), name='set-status-rental'),
    path('set-status-ride/', csrf_exempt(SetStatusRide), name='set-status-ride'),
    path('find-all-riderequests/', never_cache(csrf_exempt(GetAllRides.as_view())), name='find-all-rides'),
    path('find-all-rentalrequests/', never_cache(csrf_exempt(GetAllRentalBookings.as_view())), name='find-all-rentals'),
    path('find-all-rentals/', never_cache(csrf_exempt(GetAllRentals.as_view())), name='find-all-rentals'),
    path('order-payment/', OrderPayment.as_view(), name='order-payment'),
    path('order-verify/', OrderVerify.as_view(), name='order-verify'),
]

