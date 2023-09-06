#create a model named ride in service/models/ride.py
from django.db import models
from user.models.user_info import UserInfo
from gig.models import Worker

class Ride(models.Model):
    class stats(models.IntegerChoices):
        PENDING = 0
        ACCEPTED= 1
        COMPLETED = 2
        CANCELLED = 3
        REJECTED=4
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    start_coordinates = models.CharField(max_length=255)
    end_coordinates = models.CharField(max_length=255)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=stats.choices, default=stats.PENDING)
    distance = models.FloatField(default=0)
    price = models.FloatField(default=0)
    rating = models.FloatField(default=5)

    def __str__(self):
        return str(self.id)+str(self.amount)