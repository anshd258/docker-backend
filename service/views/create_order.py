from django.http import JsonResponse, HttpResponse

from user.models.user_info import UserInfo
from ..models import Order, Location
from django.views import View
from ..serializers import OrderSerializer
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

class CreateOrder(View):
    def get(self, request):
        try:
            location = Location.objects.get(name=request.GET["location"])
            print(location.id)
            user_id = request.session.get('userdata', {}).get('user', {}).get('id', None)
            if not user_id:
                user_id = request.GET["user_id"]
            user = User.objects.get(pk=user_id)
            print(user.id)
            uinfo=get_object_or_404(UserInfo,user=user)
            order = Order.objects.create(location=location, user=uinfo)
            order.save()
            print(order.id)
            order_dict = OrderSerializer(order).data
            order_dict = {
                'order': order_dict
            }
            return JsonResponse(order_dict)
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)
