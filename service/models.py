from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.TextField()
    description = models.TextField()
    address = models.TextField(max_length=255)
    max_persons = models.IntegerField()
    location_type = models.TextField()
    surge = models.FloatField(default=1.0)


class Provider(models.Model):
    business_name = models.TextField()
    provider_name = models.TextField()
    max_serving_capacity = models.IntegerField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


class Item(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.TextField()
    desc = models.TextField()
    price = models.FloatField()
    options = models.JSONField()


class ServiceArea(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)


