import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from user.models.user_info import UserInfo
from ..models import *
from ..serializers import *
from django.views import View
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

class GetAllRides(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            suser=request.user
            user=get_object_or_404(UserInfo,user=suser)
            rides = Ride.objects.filter(user=user)
            return JsonResponse({"riderequests": RideSerializer(rides, many=True).data})
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)