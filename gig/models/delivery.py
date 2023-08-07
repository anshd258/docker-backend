from django.db import models
from .job import Job
class Delivery(models.Model):
    class service_type(models.IntegerChoices):
        FOOD_DELIVERY=1
        TRANSPORT=2
    job=models.ForeignKey(Job,on_delete=models.CASCADE)
    service_type=models.PositiveSmallIntegerField(choices=service_type.choices, default=service_type.FOOD_DELIVERY)
    amount=models.DecimalField(max_digits=10,decimal_places=2)
    date=models.DateTimeField(auto_now=True)
    class Meta:
        verbose_name_plural='Deliveries'
    def __str__(self):
        return str(self.job.id)