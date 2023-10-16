from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from service.models import Order
from service.serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from user.models import UserInfo

class GetUserOrder(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        try:
            su = request.user
            user=UserInfo.objects.get(user=su)
            orders = Order.objects.filter(user=user)
            serialized_orders = OrderSerializer(orders, many=True).data
            return Response(serialized_orders, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
