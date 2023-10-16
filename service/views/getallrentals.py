from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from service.models import Rental
from service.serializers import RentalSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from user.models import UserInfo

class GetAllRentals(APIView):
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]
    def get(self, request):
        try:
            rentals=Rental.objects.all()
            serialized_rentals = RentalSerializer(rentals, many=True).data
            return Response(serialized_rentals, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)