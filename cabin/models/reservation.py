from django.db import models
from django.contrib.auth.models import User
from cabin.models.location import Location


class Reservation(models.Model):
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    price = models.IntegerField()
    adults = models.IntegerField()
    children = models.IntegerField()
    checkin = models.DateField()
    checkout = models.DateField()
    rooms = models.IntegerField()
    