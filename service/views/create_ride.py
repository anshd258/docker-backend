import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from ..serializers import RideSerializer
from ..models import Ride
from user.models import UserInfo

def CreateRide(request):
    if request.method=='POST':
        try:
            body=json.loads(request.body)
            user_id=body['user_id']
            user=get_object_or_404(UserInfo,pk=user_id)
            start_location=body['start_location']
            end_location=body['end_location']
            start_coordinates=body['start_coordinates']
            end_coordinates=body['end_coordinates']
            price=body['price']
            ride=Ride.objects.create(user=user,start_location=start_location,end_location=end_location,start_coordinates=start_coordinates,end_coordinates=end_coordinates,price=price)
            ride.save()
            return JsonResponse({'ride':RideSerializer(ride).data})
        except Exception as e:
            return JsonResponse({'error':str(e)},status=404)