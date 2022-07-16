from django.http import JsonResponse
from cabin.models import Reservation
from django.contrib.auth.models import User
from cabin.serializers import ReservationSerializer
from rest_framework.views import APIView
from user.authentication import BearerAuthentication
from rest_framework.permissions import IsAuthenticated


class GetReservations(APIView):

    authentication_classes = [BearerAuthentication]
    permission_classes = [IsAuthenticated]

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
