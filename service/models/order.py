from django.db import models
from .location import Location
from .item import Item
from django.dispatch import receiver
from django.db.models import Sum
from django.db.models.signals import post_save
from django.contrib.auth.models import User


class Order(models.Model):
    class Status(models.IntegerChoices):
        HOLD = 1  # while adding items
        CONFIRMED = 2  # while final payment is being made
        PROCESSING = 3  # final payment done and order pending service
        READY = 4  # order is ready for delivery to customer
        DELIVERED = 5  # order is delivered to customer
        COMPLETED = 6  # customer has rated the order and closed it
        FAILED = 0  # failed payment

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    discount = models.FloatField(default=0.0)
    subtotal = models.FloatField(default=0)
    taxes = models.FloatField(default=0)
    charges = models.FloatField(default=0)
    comments = models.TextField(max_length=255, null=True, blank=True)
    total = models.FloatField(default=0.0)
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.HOLD)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rating = models.FloatField(null=True, blank=True)

    def __str__(self):
        return str(self.pk) + " - " + str(self.user) + " : " + str(self.total)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name="items", null=True, blank=True)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="order_items")
    option = models.JSONField(blank=True, null=True)
    listed_price = models.FloatField()
    total = models.FloatField()
    discount = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    quantity = models.IntegerField()


@receiver(post_save, sender=OrderItem)
def update_total(sender, instance, **kwargs):
    order = instance.order
    items = sender.objects.filter(order=order)
    order.subtotal = items.aggregate(Sum('total'))['total__sum']
    order.discount = items.aggregate(Sum('discount'))['discount__sum']
    order.total = order.subtotal - order.discount if order.subtotal > order.discount else 0
    order.taxes = order.total * 0.18
    order.total += order.taxes
    post_save.disconnect(update_total, sender=OrderItem)
    order.save()
    post_save.connect(update_total, sender=OrderItem)
