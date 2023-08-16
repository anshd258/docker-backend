from django.db import models

from cabin.models.location import Location

class Property(models.Model):
    class rating(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='property')
    name = models.TextField()
    price=models.IntegerField()
    property_address = models.TextField()
    photo = models.TextField()
    property_type = models.TextField()
    rooms = models.IntegerField()
    overallrating = models.PositiveSmallIntegerField(choices=rating.choices, default=rating.FIVE)
    description = models.TextField()
    transportation_cost = models.IntegerField()
    meal_cost = models.IntegerField()
    def __str__(self):
        return self.name