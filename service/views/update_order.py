import os
from django.views import View
from ..models import Order, OrderItem
from gig.models import Job, Worker
from django.core import serializers
from django.http import JsonResponse
from ..serializers import OrderSerializer
import json
from gig.views import assign_job, find_workers
from gig.serializers import WorkerSerializer
from user.otp_generation import GenerateMsg,GenerateLink
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
class UpdateOrder(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    @staticmethod
    def create_gig_job(order):
        job = Job(order=order)
        job.commission = order.charges + 0.1 * (order.subtotal - order.discount)
        job.save()
        workers= find_workers.FindWorkers.filter_worker(None, order.location,1)
        if len(workers) > 0:
            link=GenerateLink(job.id)
            for i in workers:
                msg=GenerateMsg(i.user_info.contact, "You have been assigned a job. Please click on the link to accept the job: "+os.environ.get('CLIENT_BASE','http://localhost:60606/')+"services/?uid="+link+"&workerid="+str(i.id))
                msg.send_message()
            return JsonResponse({"status": "success"}, status=200)
        else:
            print('not available')
            return JsonResponse({"status": "No workers found"}, status=404)
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
