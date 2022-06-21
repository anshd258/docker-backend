from django.http import JsonResponse
from django.views import View
from django.core import serializers
from cabin.models import Reservation
import json


class GetReservations(View):
    def get(self, request):
        reservations = Reservation.objects.filter(user=request.user).all()
        return JsonResponse({"status": json.loads(serializers.serialize("json", reservations))})

    def post(self):
        pass
