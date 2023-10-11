from django.db import models

from user.models.user_info import UserInfo


class Rental(models.Model):
    name=models.CharField(max_length=255)
    description=models.TextField(max_length=255,null=True,blank=True)
    price=models.FloatField(default=0)
    image=models.TextField(null=True,blank=True)
    engineCapacity=models.CharField(max_length=255,null=True,blank=True)
    mileage=models.CharField(max_length=255,null=True,blank=True)
    fuelType=models.CharField(max_length=255,null=True,blank=True)
    seatingCapacity=models.IntegerField(default=2)
    _type=models.CharField(max_length=255,null=True)
    quantity=models.IntegerField(default=0)
    def __str__(self):
        return str(self.name)
    
class RentalBooking(models.Model):
    class stats(models.IntegerChoices):
        PENDING = 0
        ACCEPTED= 1
        COMPLETED = 2
        CANCELLED = 3
        REJECTED=4
    user=models.ForeignKey(UserInfo,on_delete=models.CASCADE)
    rental=models.ForeignKey(Rental,on_delete=models.CASCADE)
    start_location = models.CharField(max_length=255)
    end_location = models.CharField(max_length=255)
    start_coordinates = models.CharField(max_length=255)
    end_coordinates = models.CharField(max_length=255)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    status = models.PositiveSmallIntegerField(choices=stats.choices, default=stats.PENDING)
    distance = models.FloatField(default=0)
    rating = models.FloatField(default=0)
