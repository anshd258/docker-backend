from django.http import JsonResponse
from ..serializers import OrderSerializer, OrderItemSerializer
from django.views import View
from ..models import Order, OrderItem
import json

# STILL WORKING ON THIS WILL COMPLETE THIS BY TOMORROW
class GetOrders(View):
    def get(self, request):
        try:
            user_id = request.GET["id"]
            orders = Order.objects.filter(user_id=user_id).all()
            order_dict = OrderSerializer(orders, many=True).data
            i = 0
            for order in orders:
                order_item = OrderItem.objects.filter(order=order).exclude(total=0).first()
                order_dict[i]['items'] = OrderItemSerializer(order_item, many=False).data
                i += 1
            return JsonResponse({"orders": order_dict})
        except Exception as e:
            return JsonResponse(str(e), status=404)
