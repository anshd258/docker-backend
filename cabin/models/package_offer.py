from django.db import models

class Package(models.Model):
    name = models.TextField()
    description = models.TextField()
    amount = models.BigIntegerField()
    duration = models.FloatField()
    discount = models.IntegerField()
    cabin_type = models.IntegerField()