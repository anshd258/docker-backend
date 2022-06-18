from django.db import models
from django.contrib.auth.models import User

class Location(models.Model):
    name = models.TextField()
    description = models.TextField()
    location = models.TextField()
    photo = models.TextField()
    cabin_type = models.TextField()
    rooms = models.IntegerField()