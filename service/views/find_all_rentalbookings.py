from rest_framework.response import Response
from rest_framework import status
from ..models import RentalBooking
from ..serializers import RentalBookingSerializer
from django.views import View
from django.http import JsonResponse

class GetAllRentalBookings(View):
    def get(self, request):
        try:
            user=request.GET['user_id']
            rentals = RentalBooking.objects.filter(user__id=user)
            print(rentals)
            serializer = RentalBookingSerializer(rentals, many=True)
            return JsonResponse({"rentalrequests": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=status.HTTP_404_NOT_FOUND)
    
