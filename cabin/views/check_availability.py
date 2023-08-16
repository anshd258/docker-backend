from django.http import JsonResponse
from django.views import View
from cabin.availability.calculate_availability import CalculateAvailability


class CheckAvailability(View):

    def get(self, request):
        return JsonResponse({"status": CalculateAvailability(
            request.GET['id'],
            request.GET['rooms'],
            request.GET['checkin'],
            request.GET['checkout']
        )})
