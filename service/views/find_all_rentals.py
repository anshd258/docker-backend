from django.views import View
from ..models import Rental
from ..serializers import RentalSerializer
from django.http import JsonResponse
class GetAllRentals(View):
    def get(self, request):
        try:
            rentals = Rental.objects.all()
            serializer = RentalSerializer(rentals, many=True)
            return JsonResponse({"rentals": serializer.data})
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)