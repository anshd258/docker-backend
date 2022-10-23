from django.http import JsonResponse
from ..serializers import OrderSerializer, OrderItemSerializer
from django.views import View
from ..models import Order, OrderItem
from django.db.models import Q
from user.models import UserInfo, User
import json


class FindOrders(View):
    def get(self, request):
        # TODO : Deprecate Get call for this
        try:
            order_id = request.GET["id"]
            order = Order.objects.filter(pk=order_id).first()
            order_dict = OrderSerializer(order).data
            order_dict = {
                'order': order_dict
            }
            return JsonResponse(order_dict)
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)

    def post(self, request):
        try:
            body = json.loads(request.body)
            orders = None
            result = []
            if 'id' in body:
                orders = Order.objects.filter(pk=body['id'])
            if 'phone' in body:
                user_info = UserInfo.objects.get(contact=body['phone'])
                orders = Order.objects.filter(user=user_info.user)

            result = {"orders": OrderSerializer(orders, many=True).data}
            return JsonResponse(result)

        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)
