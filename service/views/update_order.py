from django.views import View
from ..models import Order, OrderItem
from gig.models import Job, Worker
from django.core import serializers
from django.http import JsonResponse
from ..serializers import OrderSerializer
import json


class UpdateOrder(View):
    @staticmethod
    def create_gig_job(order):
        job = Job(order=order)
        job.commission = order.charges + 0.1 * (order.subtotal - order.discount)
        job.save()

    def post(self, request):
        try:
            body = json.loads(request.body)
            order = Order.objects.filter(pk=body["order"]["id"])
            del body["order"]["id"]
            order.update(**body["order"])
            order[0].save()
            if order[0].status == Order.Status.CONFIRMED:
                UpdateOrder.create_gig_job(order[0])
            order_dict = OrderSerializer([order[0]], many=True).data[0]
            return JsonResponse(order_dict)
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)
