import json
from django.http import JsonResponse
from ..models import *
from ..serializers import *
from django.views import View
class GetAllRides(View):
    def get(self, request):
        try:
            user=request.GET['user_id']
            rides = Ride.objects.filter(user__id=user)
            return JsonResponse({"riderequests": RideSerializer(rides, many=True).data})
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)