from django.contrib import admin
from .models import Provider, Item, Location, ServiceArea

# Register your models here.
admin.site.register(Provider)
admin.site.register(Item)
admin.site.register(Location)
admin.site.register(ServiceArea)
