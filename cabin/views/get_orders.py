from django.http import JsonResponse
from django.views import View
from django.core import serializers
from cabin.models import Reservation
import json
from django.contrib.auth.models import User


class GetReservations(View):
    def get(self, request):
        user = None
        try:
            user = User.objects.filter(id=request.GET["user_id"]).first()
        except:
            user = request.user
        reservations = Reservation.objects.filter(user=user).all()
        return JsonResponse({"status": json.loads(serializers.serialize("json", reservations,
                                                                        fields=(
                                                                            'location', 'price', 'adults', 'children',
                                                                            'checkin', 'checkout', 'rooms')
                                                                        ))})

    def post(self):
        pass
