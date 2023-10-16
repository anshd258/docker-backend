from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from service.models import Ride
from service.serializers import RideSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from user.models import UserInfo

class GetUserRide(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        try:
            su = request.user
            user=UserInfo.objects.get(user=su)
            rides = Ride.objects.filter(user=user)
            serialized_rides = RideSerializer(rides, many=True).data
            return Response(serialized_rides, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)
