import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from ..serializers import RideSerializer
from ..models import Ride
from user.models import UserInfo
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes, api_view

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def CreateRide(request):
    if request.method=='POST':
        try:
            body=json.loads(request.body)
            user=request.user
            if not user.is_authenticated:
                return JsonResponse({'error':'User not authenticated'},status=401)
            user=get_object_or_404(UserInfo,user=user)
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