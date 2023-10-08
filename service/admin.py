from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Provider)
admin.site.register(FoodItem)
admin.site.register(Location)
admin.site.register(ServiceArea)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Discount)
admin.site.register(Ride)
admin.site.register(Rental)
admin.site.register(RentalBooking)
