from django.db import models
from .location import Location


class ProviderManager(models.Manager):
    def get_by_natural_key(self, business_name, provider_name):
        return self.get(business_name=business_name, provider_name=provider_name)


class Provider(models.Model):
    business_name = models.CharField(max_length=100)
    provider_name = models.CharField(max_length=100)
    max_serving_capacity = models.IntegerField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="location")

    objects = ProviderManager()

    class Meta:
        unique_together = [['business_name', 'provider_name']]
