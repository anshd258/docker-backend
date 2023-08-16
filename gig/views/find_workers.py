from django.http import JsonResponse
from django.views import View
from ..models import Worker
from ..serializers import WorkerSerializer
import json

class FindWorkers(View):
    def get(self, request):
        try:
            workers = Worker.objects.all()
            response = WorkerSerializer(workers, many=True).data
            return JsonResponse({"status": "success", "workers": response}, status=200)
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)

    def post(self, request):
        body = json.loads(request.body)
        try:
            if 'status' in body:
                workers = Worker.objects.filter(location=body['location'],status=body['status'])
            else:
                workers = Worker.objects.filter(location=body['location'])
            response = WorkerSerializer(workers, many=True).data
            return JsonResponse({"status": "success", "workers": response}, status=200)
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)
    def filter_worker(self, location,status):
        try:
            if status is not None:
                workers = Worker.objects.filter(service_areas=location,status=status)
            else:
                workers = Worker.objects.filter(location=location)
            return workers
        except Exception as e:
            print(str(e))