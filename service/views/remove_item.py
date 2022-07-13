from django.views import View
import json
from ..models import Order, OrderItem
from ..serializers import OrderItemSerializer
from django.http import JsonResponse


class RemoveItem(View):
    def post(self, request):
        try:
            body = json.loads(request.body)
            order = Order.objects.get(pk=body['order']['id'])
            order_items = body['order']['items']
            result = [order.remove_item(item['id'], item['quantity']) for item in order_items]
            order.save()
            return JsonResponse(OrderItemSerializer(result, many=True).data, safe=False)
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)
