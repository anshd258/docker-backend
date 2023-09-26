from django.views import View
from django.http import JsonResponse
from ..orders.order_management import OrderManagement
import json
from ..serializers import OrderSerializer
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
class AddItems(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            body = json.loads(request.body)
            order_manager = OrderManagement(body["order"]["id"])
            for item in body["order"]["items"]:
                order_manager.add_item(item, item["final_price"], item.get("quantity", 1),
                                       item.get("discount", 0.0), item.get("option", None))
            order_dict = OrderSerializer(order_manager.get_order()).data
            return JsonResponse({"status": "success"})
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)
