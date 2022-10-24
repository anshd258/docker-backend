from django.db import models
from .worker import Worker
from service.models import Order


class Job(models.Model):
    worker = models.ForeignKey(Worker, related_name='jobs', on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, related_name='gig_jobs', on_delete=models.CASCADE)
    commission = models.DecimalField(decimal_places=2, default=0.0, max_digits=10)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

