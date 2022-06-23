from django.db import models


class Location(models.Model):
    name = models.TextField()
    description = models.TextField()
    address = models.TextField(max_length=255)
    max_persons = models.IntegerField()
    location_type = models.TextField()
    surge = models.FloatField(default=1.0)
