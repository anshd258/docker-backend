from django.contrib import admin
from django.contrib import admin
from .models import *
# Register your models here.

# Register your models here.
admin.site.register(Location)
admin.site.register(Reservation)
admin.site.register(PaymentStatus)
admin.site.register(Package)
admin.site.register(Property)
admin.site.register(LocationMetaData)
admin.site.register(PropertyMetaData)
admin.site.register(PropertyReview)
admin.site.register(Room)