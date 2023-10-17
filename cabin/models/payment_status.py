from datetime import datetime
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from .reservation import Reservation


class PaymentStatus(models.Model):
    payment_ref_id = models.CharField(max_length=200)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, related_name='reservation')
    status = models.BooleanField(default=False)
    amount = models.IntegerField()
    create_time = models.DateTimeField(default=datetime(2021, 1, 1, 0, 0, 0, 0))
    update_time = models.DateTimeField(default=datetime(2021, 1, 1, 0, 0, 0, 0))


    