from django.db import models
from .provider import Provider


class FoodItem(models.Model):
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE, related_name="provider")
    name = models.CharField(max_length=100)
    desc = models.TextField(max_length=255, blank=True, null=True)
    price = models.FloatField(default=0)
    category = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    options = models.JSONField(null=True, blank=True)
    veg = models.BooleanField(default=False)
    available = models.BooleanField(default=True)
    image=models.ImageField(upload_to='images/', blank=True, null=True)

    def __str__(self):
        return str(self.name) + " by " + str(self.provider.business_name)
