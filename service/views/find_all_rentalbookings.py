from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status

from user.models.user_info import UserInfo
from ..models import RentalBooking
from ..serializers import RentalBookingSerializer
from django.views import View
from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
class GetAllRentalBookings(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            suser=request.user
            user=get_object_or_404(UserInfo,user=suser)
            rentals = RentalBooking.objects.filter(user=user)
            print(rentals)
            serializer = RentalBookingSerializer(rentals, many=True)
            return JsonResponse({"rentalrequests": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=status.HTTP_404_NOT_FOUND)
    
