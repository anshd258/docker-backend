from django.http import JsonResponse
from django.core import serializers
import json
from django.views import View
from ..models import Order


class FindOrders(View):
    def get(self, request):
        order_id = request.GET["id"]
        order = Order.objects.get(pk=order_id)
        order_dict = json.loads(serializers.serialize('json', [order]))[0]
        order_dict["order"] = order_dict["fields"]
        del order_dict["fields"]
        order_dict["order"]["id"] = order_dict["pk"]
        return JsonResponse(order_dict)
