from django.views import View
import json
from ..models import Order, OrderItem
from ..serializers import OrderItemSerializer
from ..orders.order_management import OrderManagement
from django.http import JsonResponse


class RemoveItem(View):
    def post(self, request):
        try:
            body = json.loads(request.body)
            order_manager = OrderManagement(body['order']['id'])
            order_items = body['order']['items']
            [order_manager.remove_item(item['id'], item['quantity']) for item in order_items]
            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)
