from django.http import JsonResponse
from ..serializers import OrderSerializer, OrderItemSerializer
from django.views import View
from ..models import Order, OrderItem


class GetOrders(View):
    def get(self, request):
        try:
            user_id = request.GET["id"]
            orders = Order.objects.filter(user_id=user_id).all()
            order_dict = OrderSerializer(orders, many=True).data
            i = 0
            for order in orders:
                order_item = OrderItem.objects.filter(order=order).exclude(total=0).all()
                order_dict[i]['items'] = OrderItemSerializer(order_item, many=True).data
                i += 1
            return JsonResponse({"orders": order_dict})
        except Exception as e:
            return JsonResponse(str(e), status=404)
