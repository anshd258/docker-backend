from django.contrib import admin
from cabin.models.location import Location
from cabin.models.reservation import Reservation
from cabin.models.payment_status import PaymentStatus
# Register your models here.

admin.site.register(Location)
admin.site.register(Reservation)
admin.site.register(PaymentStatus)