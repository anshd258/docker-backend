from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from ..serializers import OrderSerializer, OrderItemSerializer
from django.views import View
from ..models import Order, OrderItem
from django.db.models import Q
from user.models import UserInfo, User
import json

class FindAllOrders(View):
    def get(self, request):
        id=request.GET['phone']
        user=get_object_or_404(UserInfo,contact=id)
        orders=Order.objects.filter(user=user)
        ser_orders=OrderSerializer(orders,many=True).data
        return JsonResponse({'orders':ser_orders})
