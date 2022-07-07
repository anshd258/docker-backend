from django.views import View
from ..models import Order, OrderItem
from django.core import serializers
from django.http import JsonResponse
from ..serializers import OrderSerializer
import json


class UpdateOrder(View):
    def post(self, request):
        body = json.loads(request.body)
        order = Order.objects.filter(pk=body["order"]["id"])
        order_items = [OrderItem.objects.get(pk=item['id']) for item in body["order"]["items"]]
        del body["order"]["items"]
        del body["order"]["id"]
        order.update(**body["order"])
        order[0].items.set(order_items)
        order[0].save()
        order_dict = OrderSerializer([order[0]], many=True).data[0]
        return JsonResponse(order_dict)
