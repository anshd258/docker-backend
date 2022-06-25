from django.db import models
from .location import Location


class Provider(models.Model):
    business_name = models.CharField(max_length=100)
    provider_name = models.CharField(max_length=100)
    max_serving_capacity = models.IntegerField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)