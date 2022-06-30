from django.http import JsonResponse
from django.views import View
from cabin.models import PaymentStatus
from cabin.serializers import PaymentStatusSerializer


class CheckPaymentStatus(View):

    def get(self, request):
        reservation_id = request.GET["reservation_id"]
        payment = PaymentStatus.objects.filter(reservation_id=reservation_id).first()
        return JsonResponse(PaymentStatusSerializer(payment, many=False).data)

    def post(self):
        pass
