import json
from django.core import serializers


class Orders:
    def __init__(self, reservations):
        self.__orders__ = json.loads(serializers.serialize("json", reservations,
                                                           fields=(
                                                               'id', 'location', 'price', 'adults', 'children',
                                                               'checkin', 'checkout', 'rooms')
                                                           ))

    def get_orders(self):
        orders = []
        for order in self.__orders__:
            order["fields"]["id"] = order["pk"]
            orders.append(order["fields"])
        return orders
