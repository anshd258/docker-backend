from django.db import models
from .location import Location
from .item import Item
from django.dispatch import receiver
from django.db.models import Sum
from django.db.models.signals import post_save
import uuid


class OrderItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="item")
    option = models.JSONField(blank=True, null=True)
    listed_price = models.FloatField()
    total = models.FloatField()
    discount = models.FloatField(default=0)
    rating = models.FloatField(default=0)
    quantity = models.IntegerField()


class Order(models.Model):
    class Status(models.IntegerChoices):
        HOLD = 1  # while adding items
        CONFIRMED = 2  # while final payment is being made
        PROCESSING = 3  # final payment done and order pending service
        READY = 4  # order is ready for delivery to customer
        DELIVERED = 5  # order is delivered to customer
        COMPLETED = 6  # customer has rated the order and closed it
        FAILED = 0  # failed payment

    # add user field with foreign key to user
    items = models.ManyToManyField(OrderItem)
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

    def add_item(self, item_id, listed_price, quantity=1, discount=0, option=None):
        item = Item.objects.get(pk=item_id)
        self.save()
        option_prices = 0
        option = None if option == {} else option
        if option:
            option_prices = sum(option.values())
        order_item = self.items.filter(item=item)[0] if self.items.filter(item=item).exists() else None
        if order_item and order_item.option == option:
            order_item.quantity += 1
            order_item.listed_price += listed_price
            order_item.total += listed_price + option_prices
            order_item.discount = discount
        else:
            order_item = OrderItem()
            order_item.item = item
            order_item.quantity = quantity
            order_item.listed_price = listed_price
            order_item.total = listed_price + option_prices
            order_item.discount = discount

        order_item.total = 0 if order_item.total < 0 else order_item.total
        order_item.save()

        self.items.add(order_item)
        self.save()
        return self


@receiver(post_save, sender=Order)
def update_total(sender, instance, **kwargs):
    subtotal = instance.items.aggregate(Sum('total'))['total__sum']
    discounts = instance.items.aggregate(Sum('discount'))['discount__sum']
    instance.discount = discounts if discounts else 0
    instance.subtotal = subtotal if subtotal else 0
    instance.total = instance.subtotal - instance.discount
    instance.taxes = instance.total * 0.18
    post_save.disconnect(update_total, sender=Order)
    instance.save()
    post_save.connect(update_total, sender=Order)

