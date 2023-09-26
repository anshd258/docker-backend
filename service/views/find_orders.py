from django.http import JsonResponse
from ..serializers import OrderSerializer, OrderItemSerializer
from django.views import View
from ..models import Order, OrderItem
from django.db.models import Q
from django.shortcuts import get_object_or_404
from user.models import UserInfo, User
import json
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class FindOrder(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            body = json.loads(request.body)
            orders = None
            order = get_object_or_404(Order, id=body['id'])
            result = {"order": OrderSerializer(order, many=False).data}
            return JsonResponse(result)

        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)
