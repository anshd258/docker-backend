from django.http import JsonResponse
from django.views import View
from cabin.models import PaymentStatus


class CheckPaymentStatus(View):

    def get(self, request):
        reservation_id = request.GET["id"]
        if PaymentStatus.objects.filter(reservation_id=reservation_id).first().status:
            return JsonResponse({"status": "Paid"})
        else:
            return JsonResponse({"status": "Not Paid"})

    def post(self):
        pass
