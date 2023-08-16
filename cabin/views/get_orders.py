from django.http import JsonResponse
from cabin.models import Reservation
from user.models import UserInfo
from django.views import View
from cabin.models import Reservation, Property
from django.contrib.auth.models import User
from user.models import UserInfo
from cabin.serializers import ReservationSerializer
from rest_framework.views import APIView
from user.authentication import BearerAuthentication
from rest_framework.permissions import IsAuthenticated




class GetReservations(APIView):

    authentication_classes = [BearerAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        try:
            user = None

            if request.GET.get("user_id"):
                user_id = request.GET["user_id"]
                user = User.objects.filter(id=user_id).first()

            elif request.GET.get("email"):
                email_id = request.GET["email"]
                user = User.objects.filter(email=email_id).first()

            elif request.GET.get("phone"):
                phone = request.GET["phone"]
                user = UserInfo.objects.filter(contact=phone).first().user

            elif request.GET.get("location"):
                location = Property.objects.filter(name=request.GET["location"]).first()
                reservations = Reservation.objects.filter(property=location).all()
                return JsonResponse({"reservations": ReservationSerializer(reservations, many=True).data})

            reservations = Reservation.objects.filter(user=user).all()
            return JsonResponse({"reservations": ReservationSerializer(reservations, many=True).data})

        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)

