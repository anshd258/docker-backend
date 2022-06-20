from django.db import models

class Location(models.Model):
    name = models.TextField()
    description = models.TextField()
    location = models.TextField()
    photo = models.TextField()
    cabin_type = models.TextField()
    rooms = models.IntegerField()