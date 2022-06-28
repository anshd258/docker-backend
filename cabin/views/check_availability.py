from django.http import JsonResponse
from django.views import View
from cabin.availability.calculate_availability import CalculateAvailability


class CheckAvailability(View):

    def get(self, request):
        if CalculateAvailability(
                                request.GET['id'],
                                request.GET['rooms'],
                                request.GET['checkin'],
                                request.GET['checkout']
                                 ):
            return JsonResponse({"status": "Available"})
        else:
            return JsonResponse({"status": "Not Available"})

    def post(self):
        pass
