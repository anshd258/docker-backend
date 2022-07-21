from django.http import JsonResponse
from django.views import View
from cabin.models import Reservation, Location
from django.contrib.auth.models import User
from user.models import UserInfo
from cabin.serializers import ReservationSerializer
"""
    This function will accept following endpoints:
        /cabin/get-booking/?location=<location_name>
        /cabin/get-booking/?phone=<phone_number>
        /cabin/get-booking/?email=<email>
        /cabin/get-booking/?user_id=<user_id>
"""


class GetReservations(View):
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
                location = Location.objects.filter(name=request.GET["location"]).first()
                reservations = Reservation.objects.filter(location=location).all()
                return JsonResponse({"reservations": ReservationSerializer(reservations, many=True).data})

            reservations = Reservation.objects.filter(user=user).all()
            return JsonResponse({"reservations": ReservationSerializer(reservations, many=True).data})

        except Exception as e:
            print(e)
            return JsonResponse({"status": e})

