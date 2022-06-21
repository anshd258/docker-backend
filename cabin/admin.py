from django.contrib import admin
from cabin.models import Location, Reservation, PaymentStatus

admin.site.register(Location)
admin.site.register(Reservation)
admin.site.register(PaymentStatus)
