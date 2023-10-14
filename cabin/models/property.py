from django.db import models

from cabin.models.location import Location

class Property(models.Model):
    class rating(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
    class desc(models.IntegerChoices):
        FAMILY = 1
        ADVENTURE = 2
        LAVISH=3
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='property')
    name = models.TextField()
    price=models.IntegerField()
    property_address = models.TextField()
    photo = models.TextField()
    property_type = models.TextField()
    rooms = models.IntegerField()
    overallrating = models.PositiveSmallIntegerField(choices=rating.choices, default=rating.FIVE)
    description = models.PositiveSmallIntegerField(choices=desc.choices, default=desc.FAMILY)
    transportation_cost = models.IntegerField()
    meal_cost = models.IntegerField()
    directions= models.TextField()
    def __str__(self):
        return self.name