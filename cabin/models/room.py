from django.db import models
from cabin.models.property import Property
from django.db.models.signals import post_save
from django.dispatch import receiver
class Room(models.Model):
    _property=models.ForeignKey(Property,on_delete=models.CASCADE)
    _type=models.CharField(max_length=100)
    price=models.IntegerField()
    available=models.IntegerField()
    images=models.TextField()
    name=models.CharField(max_length=100)
    bed_type=models.CharField(max_length=100)
    occuptancy=models.IntegerField()
    def __str__(self):
        return str(self._property.id) + " - " + str(self._type)

@receiver(post_save, sender=Room)
def update_rooms(sender, instance, created, **kwargs):
    if created:
        instance._property.rooms+=instance.available
        instance._property.save()