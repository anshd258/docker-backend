from django.http import JsonResponse
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
        return JsonResponse(order_json, safe=False)
