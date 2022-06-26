from django.views import View
from django.http import JsonResponse
from django.core import serializers
from ..models import Order
import json


class AddItems(View):
    def post(self, request):
        body = json.loads(request.body)
        order = Order.objects.get(pk=body["order"]["id"])
        for item in body["order"]["items"]:
            order = order.add_item(item["id"], item["final_price"], item["discount"], item["option"])
        order_dict = json.loads(serializers.serialize('json', [order]))[0]
        order_dict["order"] = order_dict["fields"]
        del order_dict["fields"]
        order_dict["order"]["id"] = order_dict["pk"]
        return JsonResponse(order_dict)
