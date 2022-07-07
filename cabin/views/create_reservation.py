from django.http import JsonResponse
from django.views import View
from cabin.models import Reservation, PaymentStatus
from cabin.availability import CalculateAvailability
from cabin.serializers import PaymentStatusSerializer,ReservationSerializer
import json

class CreateReservation(View):
    def get(self, request):
        pass

    def post(self, request):
        obj = json.loads(request.body)
        if not CalculateAvailability(
                obj['location_id'],
                obj['rooms'],
                obj['checkin'],
                obj['checkout']
                ):
            return JsonResponse({'status': 'Rooms are not available'})

        reservation = Reservation.objects.create(
            location_id=obj["location_id"],
            user_id=obj["user_id"],
            price=obj["price"],
            adults=obj["adults"],
            children=obj["children"],
            checkin=obj["checkin"],
            checkout=obj["checkout"],
            rooms=obj["rooms"]
        )
        payment = PaymentStatus.objects.create(
            payment_ref_id="some-randomly-generated-or-some-other-string",
            reservation_id=reservation.id,
            amount=obj["price"]
        )
        return JsonResponse({
            "reservation": ReservationSerializer(reservation, many=False).data,
            "payment_status": PaymentStatusSerializer(payment, many=False).data,
        })
