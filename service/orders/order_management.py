from ..models import OrderItem, Order, Item


class OrderManagement:
    def __init__(self, order_id=None):
        self.__order__ = Order.objects.get_or_create(id=order_id)