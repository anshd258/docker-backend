from django.http import JsonResponse
from django.views import View
from ..models import Worker
from ..serializers import WorkerSerializer


class FindWorkers(View):
    def get(self, request):
        try:
            workers = Worker.objects.all()
            response = WorkerSerializer(workers, many=True).data
            return JsonResponse({"status": "success", "workers": response}, status=200)
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)

    def post(self, request):
        # TODO: Add all filtering here
        pass