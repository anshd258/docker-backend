from django.db import models
from .provider import Provider


class Item(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE,related_name="provider")
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=255)
    price = models.FloatField(default=0)
    options = models.JSONField(null=True, blank=True)

    def __str__(self):
        return str(self.name) + " by " + str(self.provider.business_name)
