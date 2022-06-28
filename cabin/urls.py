from django.urls import path
from cabin.views import CheckAvailability, CheckPaymentStatus, GetReservations, CreateReservation,PostTesting

urlpatterns = [
    path('get-room-availability/', CheckAvailability.as_view(), name='room-availability'),
    path('payment-status/', CheckPaymentStatus.as_view(), name='payment-status'),
    path('get-booking/', GetReservations.as_view(), name='payment-status'),
    path('create-booking/', CreateReservation.as_view(), name='payment-status'),
    path('post-testing/', PostTesting, name='post-testing'),
]
