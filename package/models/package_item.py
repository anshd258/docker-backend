from django.db import models


class PackageItem(models.Model):
    package_item = models.CharField(max_length=300)
    priority = models.IntegerField()
    max_guests = models.IntegerField()
    cost_price = models.IntegerField()
    duration = models.FloatField()
    min_buffer_percent = models.FloatField()
    margin_percent = models.FloatField()
    sales_price = models.FloatField()
    comments = models.TextField(blank=True)

