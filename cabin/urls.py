from django.urls import path
from cabin.views import CheckAvailability,CheckPaymentStatus,GetReservations,CreateReservation


urlpatterns = [
    path('getRoomAvailability/',CheckAvailability.as_view(),name='Room-Availability'),   
    path('paymentStatus/',CheckPaymentStatus.as_view(),name='payment-status'),   
    path('getBooking/',GetReservations.as_view(),name='payment-status'),   
    path('CreateBooking/',CreateReservation.as_view(),name='payment-status'),   
]
