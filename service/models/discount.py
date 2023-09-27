from django.db import models
from ..models import Location, FoodItem, Provider


class Discount(models.Model):
    class LinkedTo(models.IntegerChoices):
        LOCATION = 1
        ITEM = 2
        PROVIDER = 3

    code = models.CharField(unique=True,max_length=100)
    percent = models.FloatField(default=0)
    upto = models.FloatField(default=0)
    min_price = models.FloatField(default=0)
    linked_to = models.PositiveSmallIntegerField(choices=LinkedTo.choices, default=LinkedTo.ITEM)
    to_location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True, blank=True)
    to_item = models.ForeignKey(FoodItem, on_delete=models.CASCADE, null=True, blank=True)
    to_provider = models.ForeignKey(Provider, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.pk) + " - " + str(self.code)
