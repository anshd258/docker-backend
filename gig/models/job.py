from django.db import models
from .worker import Worker
from service.models import Order


class Job(models.Model):
    worker = models.ForeignKey(Worker, related_name='jobs', on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, related_name='gig_jobs', on_delete=models.CASCADE)
