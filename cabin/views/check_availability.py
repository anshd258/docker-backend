from django.http import JsonResponse
from django.views import View
from cabin.availability.calculate_availability import CalculateAvailability


class CheckAvailability(View):

    def get(self, request):
        try:
            return JsonResponse({"status": CalculateAvailability(
                request.GET['id'],
                request.GET['rooms'],
                request.GET['checkin'],
                request.GET['checkout']
            )})
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)

    def post(self):
        pass
