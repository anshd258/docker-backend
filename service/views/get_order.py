from django.views import View
from django.http import JsonResponse
from service.models import Order
from service.serializers import OrderSerializer
class GetOrder(View):
    def get(self, request):
        try:
            order_id = request.GET.get('order_id')
            order = Order.objects.get(id=order_id)
            order_serializer = OrderSerializer(order)
            return JsonResponse({"order":order_serializer.data})
        except Exception as e:
            return JsonResponse({"error":str(e)})