from django.http import JsonResponse
from django.views import View
from cabin.models import Reservation
from django.contrib.auth.models import User
from cabin.orders import Orders


class GetReservations(View):
    def get(self, request):
        user = None
        try:
            user = User.objects.filter(id=request.GET["user_id"]).first()
        except:
            user = request.user
        reservations = Reservation.objects.filter(user=user).all()
        orders = Orders(reservations)
        return JsonResponse({"orders": orders.get_orders()})

    def post(self):
        pass
