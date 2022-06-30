from django.http import JsonResponse
from django.views import View
from cabin.models import Reservation
from django.contrib.auth.models import User
from cabin.serializers import ReservationSerializer


class GetReservations(View):
    def get(self, request):
        user = None
        try:
            user_id = request.GET["user_id"]
            user = User.objects.filter(id=user_id).first()
            reservations = Reservation.objects.filter(user=user).all()
            return JsonResponse({"reservations": ReservationSerializer(reservations, many=True).data})
        except Exception as e:
            print(e)
            return JsonResponse({"status": e})


    def post(self):
        pass
