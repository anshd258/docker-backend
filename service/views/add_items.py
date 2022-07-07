from django.views import View
from django.http import JsonResponse
from ..models import Order
import json
from ..serializers import OrderSerializer


class AddItems(View):
    def post(self, request):
        body = json.loads(request.body)
        order = Order.objects.get(pk=body["order"]["id"])
        for item in body["order"]["items"]:
            order = order.add_item(item["id"], item["final_price"], item.get("quantity"), item.get("discount"), item.get("option"))
        order_dict = OrderSerializer([order], many=True).data[0]
        return JsonResponse({"order": order_dict})
