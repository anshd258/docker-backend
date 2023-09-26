from django.views import View
import json
from ..models import Order, OrderItem
from ..serializers import OrderItemSerializer
from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
class UpdateItem(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            body = json.loads(request.body)
            order_item = body['order_item']
            order_item_ob = OrderItem.objects.filter(pk=order_item['id'])
            del order_item['id']
            order_item_ob.update(**order_item)
            order_item_ob[0].save()
            return JsonResponse(OrderItemSerializer(order_item_ob[0]).data)
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)
