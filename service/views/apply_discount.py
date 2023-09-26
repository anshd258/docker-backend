from django.http import JsonResponse
from django.views import View
from ..discounts import Discounts
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class ApplyDiscount(View):
    authentication_classes = [JWTAuthentication]
    PermissionError = [IsAuthenticated]
    def get(self, request):
        try:
            order_id = request.GET["order_id"]
            discounts = Discounts(order_id, apply=True)
            return JsonResponse(discounts)
        except Exception as e:
            return JsonResponse({"error": str(e),"status":500})