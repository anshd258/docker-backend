from django.http import JsonResponse
from django.views import View
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
