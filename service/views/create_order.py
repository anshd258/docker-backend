from django.http import JsonResponse, HttpResponse
from ..models import Order, Location
from django.views import View
from ..serializers import OrderSerializer
from django.contrib.auth.models import User


class CreateOrder(View):
    def get(self, request):
        try:
            location = Location.objects.get(name=request.GET["location"])
            user_id = request.session.get('userdata', {}).get('user', {}).get('id', None)
            if not user_id:
                user_id = request.GET["user_id"]
            user = User.objects.get(pk=user_id)
            order = Order.objects.create(location=location, user=user)
            order_dict = OrderSerializer(order).data
            order_dict = {
                'order': order_dict
            }
            return JsonResponse(order_dict)
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)
