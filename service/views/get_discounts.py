from django.http import JsonResponse
from django.views import View
from ..discounts import Discounts


class GetDiscount(View):
    def get(self, request):
        try:
            order_id = request.GET["order_id"]
            discounts = Discounts(order_id, apply=False)
            return JsonResponse(discounts)
        except Exception as e:
            return JsonResponse ({"error": str(e), "status": 400})