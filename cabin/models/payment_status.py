from datetime import datetime
from django.db import models
from .reservation import Reservation


class PaymentStatus(models.Model):
    payment_ref_id = models.CharField(max_length=200)
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)
    amount = models.IntegerField()
    create_time = models.DateTimeField(default=datetime.now())
    update_time = models.DateTimeField(default=datetime.now())
