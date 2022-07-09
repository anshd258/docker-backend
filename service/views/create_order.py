from django.http import JsonResponse, HttpResponse
from ..models import Order, Location
from django.views import View
from ..serializers import OrderSerializer
from django.contrib.auth.models import User


class CreateOrder(View):
    def get(self, request):
        location = Location.objects.get(name=request.GET["location"])
        user_id = request.session.get('userdata', {}).get('user', {}).get('id', None)
        user = User.objects.get(pk=user_id)
        order = Order.objects.create(location=location, user=user)
        order_dict = OrderSerializer([order], many=True).data[0]
        order_dict = {
            'order': order_dict
        }
        return JsonResponse(order_dict)
