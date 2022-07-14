from django.http import JsonResponse
from ..serializers import OrderSerializer, OrderItemSerializer
from django.views import View
from ..models import Order, OrderItem


class FindOrders(View):
    def get(self, request):
        try:
            order_id = request.GET["id"]
            order = Order.objects.filter(pk=order_id).first()
            order_items = OrderItem.objects.filter(order=order)
            order_dict = OrderSerializer(order).data
            order_dict['items'] = OrderItemSerializer(order_items, many=True).data
            order_dict = {
                'order': order_dict
            }
            return JsonResponse(order_dict)
        except Exception as e:
            return JsonResponse(order_dict, status=404)
