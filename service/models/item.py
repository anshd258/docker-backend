from django.db import models
from .provider import Provider


class Item(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.TextField()
    desc = models.TextField()
    price = models.FloatField()
    options = models.JSONField()
