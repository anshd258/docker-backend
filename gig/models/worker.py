from django.db import models
from user.models import UserInfo


class Worker(models.Model):
    user_info = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    rating = models.FloatField(default=0.0)
