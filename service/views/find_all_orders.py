from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from ..serializers import OrderSerializer, OrderItemSerializer
from rest_framework.views import APIView
from ..models import Order, OrderItem
from django.db.models import Q
from user.models import UserInfo, User
import json
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated

class FindAllOrders(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        user=request.user
        if not user.is_authenticated:
            return JsonResponse({'error':'User not authenticated'},status=401)
        user=get_object_or_404(UserInfo,user=user)
        orders=Order.objects.filter(user=user)
        ser_orders=OrderSerializer(orders,many=True).data
        return JsonResponse({'orders':ser_orders})
