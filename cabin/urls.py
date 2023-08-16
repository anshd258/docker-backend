from django.urls import path
from cabin.views import CheckAvailability, CheckPaymentStatus, GetReservations, CreateReservation, GetAvailability, GetProperty
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('get-room-availability/', CheckAvailability.as_view(), name='room-availability'),
    path('payment-status/', CheckPaymentStatus.as_view(), name='payment-status'),
    path('get-booking/', GetReservations.as_view(), name='payment-status'),
    path('create-booking/', csrf_exempt(CreateReservation.as_view()), name='payment-status'),
    path('payment-success/', csrf_exempt(CreateReservation.success), name='payment-success'),
    path('get-availability/',GetAvailability.as_view(),name='get-availability'),
    path('get-property/',GetProperty.as_view(),name='get-property'),
]
