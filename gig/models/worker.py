from django.db import models
from user.models import UserInfo
from service.models import Location


class Worker(models.Model):
    user_info = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    service_areas = models.ManyToManyField(Location)
    earnings = models.DecimalField(decimal_places=2, default=0.0, max_digits=8)
    rating = models.DecimalField(decimal_places=2, default=0.0, max_digits=8)

    def __str__(self):
        return self.user_info.user.username + ", " + self.user_info.contact
