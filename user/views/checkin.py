from django.views import View
from django.http import JsonResponse
from service.models import Location


class Checkin(View):
    def get(self, request):
        try:
            location = Location.objects.get(name=request.GET["location"])
            no_of_persons = int(request.GET["persons"])
            location.check_in(no_of_persons)
            return JsonResponse({"status": "success"}, status=200)
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)
