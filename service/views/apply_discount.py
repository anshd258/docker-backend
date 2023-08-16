from django.http import JsonResponse
from django.views import View
from ..discounts import Discounts


class ApplyDiscount(View):
    def get(self, request):
        try:
            order_id = request.GET["order_id"]
            discounts = Discounts(order_id, apply=True)
            return JsonResponse(discounts)
        except Exception as e:
            return JsonResponse({"error": str(e),"status":500})