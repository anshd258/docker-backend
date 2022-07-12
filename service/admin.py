from django.contrib import admin
from .models import Provider, Item, Location, ServiceArea, Order, OrderItem

# Register your models here.
admin.site.register(Provider)
admin.site.register(Item)
admin.site.register(Location)
admin.site.register(ServiceArea)
admin.site.register(Order)
admin.site.register(OrderItem)
