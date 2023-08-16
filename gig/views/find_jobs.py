from django.http import JsonResponse
from django.views import View
from ..models import Job
from ..serializers import JobSerializer


class FindJobs(View):
    def get(self, request):
        try:
            jobs = Job.objects.all()
            response = JobSerializer(jobs, many=True).data
            return JsonResponse({"status": "success", "jobs": response}, status=200)
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)

    def post(self, request):
        # TODO: Add all filtering here
        pass