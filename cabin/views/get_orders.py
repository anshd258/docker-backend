from django.http import JsonResponse
from django.views import View
from cabin.models import Reservation
from user.models import UserInfo
from django.contrib.auth.models import User
from cabin.serializers import ReservationSerializer


class GetReservations(View):

    def get(self, request):
        try:
            user_id = request.GET["user_id"]
            user = User.objects.filter(id=user_id).first()
            user_info = UserInfo.objects.filter(user = user).first()
            reservations = Reservation.objects.filter(user=user_info).all()
            print(reservations)
            return JsonResponse({"reservations": ReservationSerializer(reservations, many=True).data})
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)

    def post(self):
        pass
