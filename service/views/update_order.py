from django.views import View
from ..models import Order, OrderItem
from django.core import serializers
from django.http import JsonResponse
import json


class UpdateOrder(View):
    def post(self, request):
        body = json.loads(request.body)
        order = Order.objects.filter(pk=body["order"]["id"])
        order_items = [OrderItem.objects.get(pk=item) for item in body["order"]["items"]]
        del body["order"]["items"]
        del body["order"]["id"]
        order.update(**body["order"])
        order[0].items.set(order_items)
        order[0].save()
        order_dict = json.loads(serializers.serialize('json', order))[0]
        order_dict["order"] = order_dict["fields"]
        del order_dict["fields"]
        order_dict["order"]["id"] = order_dict["pk"]
        return JsonResponse(order_dict)
