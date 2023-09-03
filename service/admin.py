from django.contrib import admin
from .models import Provider, FoodItem, Location, ServiceArea, Order, OrderItem, Discount

# Register your models here.
admin.site.register(Provider)
admin.site.register(FoodItem)
admin.site.register(Location)
admin.site.register(ServiceArea)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Discount)
