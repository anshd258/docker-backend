from django.contrib import admin
from django.contrib import admin
from .models import Location,Reservation, PaymentStatus,Package
# Register your models here.

# Register your models here.
admin.site.register(Location)
admin.site.register(Reservation)
admin.site.register(PaymentStatus)
admin.site.register(Package)
