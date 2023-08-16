from ..models import OrderItem, Order, Item


class OrderManagement:
    def __init__(self, order_id):
        self.__order__ = Order.objects.filter(pk=order_id).first()

    def get_order(self):
        return self.__order__

    def add_item(self, item, listed_price, quantity=1, discount=0, option=None):
        item = Item.objects.get(pk=item['id'])
        order_items = OrderItem.objects.filter(order=self.__order__)
        if not item:
            raise Exception("Item does not exist")
        option_prices = 0
        option = None if option == {} else option
        if option:
            option_prices = sum(option.values())

        if order_items.filter(item=item).exists():
            if option:
                order_item = order_items.filter(item=item, option=option).first()
            else:
                order_item = order_items.filter(item=item, option__isnull=True).first()
            if order_item is not None:
                order_item.quantity += quantity
                order_item.listed_price = listed_price + option_prices
                order_item.total += (listed_price + option_prices) * quantity
                order_item.discount += discount
                order_item.save()
                return self

        order_item = OrderItem()
        order_item.item = item
        order_item.quantity = quantity
        order_item.listed_price = listed_price + option_prices
        order_item.option = option
        order_item.discount = discount
        order_item.total = (listed_price + option_prices) * quantity
        order_item.order = self.__order__
        order_item.save()
        return self

    def remove_item(self, order_item_id, quantity):
        order_item = OrderItem.objects.get(pk=order_item_id)
        order_item.quantity = order_item.quantity - quantity if order_item.quantity > quantity else 0
        order_item.total = order_item.listed_price * order_item.quantity
        order_item.save()
        return self
