from django.views import View
from ..models import Order


class UpdateOrder(View):
    def post(self, request):
        order = Order.objects.get(id=request.POST["order"]["id"])
        order.update(**request.POST["order"])
        order.save()