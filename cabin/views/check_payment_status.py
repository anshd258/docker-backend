from django.http import JsonResponse
from django.views import View
from cabin.models import PaymentStatus
from django.core import serializers
import json


class CheckPaymentStatus(View):

    def get(self, request):
        reservation_id = request.GET["id"]
        it = PaymentStatus.objects.filter(reservation_id=reservation_id).all()
        return JsonResponse(
            {"status": json.loads(serializers.serialize("json", it, indent=1, use_natural_primary_keys=True))})

    def post(self):
        pass
