from django.http import JsonResponse
from django.views import View

from user.otp_generation.generate_otp import GenerateOTP
from ..models import Job, Worker
from user.models import UserInfo
import json


class AssignJob(View):
    def post(self, request):
        try:
            body = json.loads(request.body)
            job = Job.objects.filter(pk=body["job"]["id"]).first()
            worker = Worker.objects.filter(user_info__contact=body["user"]["phone"]).first()
            job.worker = worker
            job.save()
            return JsonResponse({"status": "success"}, status=200)
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)
    def assign(self,job_id, worker_contact):
        try:
            job = Job.objects.filter(pk=job_id).first()
            worker = Worker.objects.filter(user_info__contact=worker_contact).first()
            job.worker = worker
            worker.status = 2
            user=UserInfo.objects.get(pk=job.order.user.id)
            g=GenerateOTP()
            g.set_contact(user.contact)
            otp=(g.otp_generate())
            g.set_message("OTP for order" + str(job.order.id) + " is " + str(otp))
            g.send_message()
            print(otp)
            job.otp=otp
            worker.save()
            job.save()
            return 1
        except Exception as e:
            print(str(e))   
            return 0