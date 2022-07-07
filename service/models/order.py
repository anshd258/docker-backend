from django.db import models
from .location import Location
from .item import Item
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
    total = models.FloatField(default=0)
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.HOLD)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    rating = models.FloatField(null=True, blank=True)

    def add_item(self, item_id, listed_price, quantity=1, discount=0, option=None):
        item = Item.objects.get(pk=item_id)
        self.save()
        order_item = OrderItem()
        order_item.item = item
        order_item.option = option
        order_item.quantity = quantity
        order_item.listed_price = listed_price
        order_item.discount = discount
        order_item.total = listed_price - discount
        order_item.total = 0 if order_item.total < 0 else order_item.total
        order_item.save()
        self.total = self.total + order_item.total
        self.discount = self.discount + order_item.discount
        self.subtotal = self.subtotal + order_item.listed_price
        self.taxes = 1.18 * self.total
        self.items.add(order_item)
        self.save()
        return self
