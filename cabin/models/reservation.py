from django.db import models
from cabin.models.room import Room
from user.models import UserInfo
from cabin.models.property import Property

class Reservation(models.Model):
    room=models.ForeignKey(Room,on_delete=models.CASCADE,related_name='reservation')
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='reservation')
    user = models.ForeignKey(UserInfo, on_delete=models.CASCADE, related_name='user_name')
    price = models.IntegerField()
    adults = models.IntegerField()
    children = models.IntegerField()
    checkin = models.DateTimeField()
    checkout = models.DateTimeField()
    roomsbooked = models.IntegerField()
    mobile=models.CharField(max_length=10,null=True)
    whatsapp=models.CharField(max_length=10,null=True)
    
