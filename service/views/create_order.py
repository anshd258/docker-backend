from django.http import JsonResponse, HttpResponse
from rest_framework.views import APIView
from user.models.user_info import UserInfo
from ..models import Order, Location
from ..serializers import OrderSerializer
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

class CreateOrder(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            user = request.user
            if not user.is_authenticated:
                return JsonResponse({'status': 'User not authenticated'}, status=401)
            location = Location.objects.get(name=request.GET["location"])
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
