from django.http import JsonResponse, HttpResponse
from ..models import Order, Location
from django.views import View
from ..serializers import OrderSerializer
from django.core import serializers
import json


class CreateOrder(View):
    def get(self, request):
        location = Location.objects.get(name=request.GET["location"])
        order = Order.objects.create(location=location)
        order_dict = OrderSerializer([order], many=True).data[0]
        order_dict = {
            'order': order_dict
        }
        return JsonResponse(order_dict)
