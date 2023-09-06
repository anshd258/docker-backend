import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from ..serializers import RideSerializer
from ..models import Ride
def SetStatusRide(request):
    if request.method=='POST':
        try:
            body=json.loads(request.body)
            ride_id=body['ride_id']
            status=body['status']
            ride=get_object_or_404(Ride,pk=ride_id)
            ride.status=status
            ride.save()
            return JsonResponse({'ride':RideSerializer(ride).data})
        except Exception as e:
            return JsonResponse({'error':str(e)},status=404)
    return JsonResponse({'error':'Invalid Request'},status=404)