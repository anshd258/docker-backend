from django.views import View
from ..models import Rental
from ..serializers import RentalSerializer
from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
class GetAllRentals(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            rentals = Rental.objects.all()
            serializer = RentalSerializer(rentals, many=True)
            return JsonResponse({"rentals": serializer.data})
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)