from django.http import JsonResponse, HttpResponse
from ..models import Order, Location
from django.views import View
from django.core import serializers
import json


class CreateOrder(View):
    def get(self, request):
        location = Location.objects.get(name=request.GET["location"])
        # user = User.objects.get(phone=request.GET["phone"])
        order = Order.objects.create(location=location)
        order_json = serializers.serialize('json', [order])
        order_dict = json.loads(order_json)[0]
        order_dict["order"] = order_dict["fields"]
        del order_dict["fields"]
        order_dict["order"]["id"] = order_dict["pk"]
        return JsonResponse(order_dict)
