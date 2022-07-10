from django.http import JsonResponse
from ..serializers import OrderSerializer
from django.views import View
from ..models import Order


class FindOrders(View):
    def get(self, request):
        try:
            order_id = request.GET["id"]
            order = Order.objects.get(pk=order_id)
            order_dict = OrderSerializer([order], many=True).data[0]
            order_dict = {
                'order': order_dict
            }
            return JsonResponse(order_dict)
        except Exception as e:
            return JsonResponse(order_dict, status=404)
