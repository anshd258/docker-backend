from django.db import models
from django.contrib.auth.models import User
from user.models import UserInfo
from cabin.models import Location


class Reservation(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='location_name')
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='user_name')
    price = models.IntegerField()
    adults = models.IntegerField()
    children = models.IntegerField()
    checkin = models.DateTimeField()
    checkout = models.DateTimeField()
    rooms = models.IntegerField()
    mobile=models.CharField(max_length=10,null=True)
    whatsapp=models.CharField(max_length=10,null=True)
