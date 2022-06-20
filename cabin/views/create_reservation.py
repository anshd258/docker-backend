from django.http import JsonResponse
from django.views import View
from cabin.models import Reservation,PaymentStatus
from django.core import serializers
import json

class CreateReservation(View):
    def get(self,request):
        pass

    def post(self,request):
        reservation = Reservation.objects.create(
            location_id =  request.POST["location_id"],
            user_id = request.user.id,
            price = request.POST["price"],
            adults = request.POST["adults"],
            children = request.POST["children"],
            checkin = request.POST["checkin"],
            checkout = request.POST["checkout"],
            rooms = request.POST["rooms"]
        )
        PaymentStatus.objects.create(
            payment_ref_id = "some-randomly-generated-or-some-other-string",
            reservation_id = reservation.id,
            amount =request.POST["price"]
        )
        return JsonResponse({"reservation": json.loads(serializers.serialize("json",Reservation.objects.filter(id = reservation.id).all()))})
