from django.db import models


class Location(models.Model):
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(max_length=255)
    address = models.TextField(max_length=255)
    max_persons = models.IntegerField(default=0)
    location_type = models.TextField()
    surge = models.FloatField(default=1.0)
