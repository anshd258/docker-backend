from django.db import models
from cabin.models import Location

class LocationMetaData(models.Model):
    class rating(models.IntegerChoices):
        ONE = 1
        TWO = 2
        THREE = 3
        FOUR = 4
        FIVE = 5
    location=models.ForeignKey(Location,on_delete=models.CASCADE,related_name='location')
    overallrating=models.PositiveSmallIntegerField(choices=rating.choices,default=rating.FIVE)
    weather=models.TextField()
    airquality=models.TextField()
    internet= models.TextField()
    accessibility=models.PositiveSmallIntegerField(choices=rating.choices,default=rating.FIVE)
    safety=models.PositiveSmallIntegerField(choices=rating.choices,default=rating.FIVE)
    health=models.PositiveSmallIntegerField(choices=rating.choices,default=rating.FIVE)
    timezone=models.TextField()
    language=models.TextField()
    def __str__(self):
        return self.location.name