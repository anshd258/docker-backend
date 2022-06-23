from django.db import models
from .provider import Provider
from .location import Location


class ServiceArea(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
