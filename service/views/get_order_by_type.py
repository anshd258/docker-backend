import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from user.models.user_info import UserInfo
from ..models import *
from ..serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view,permission_classes

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def GetOrderByType(request):
    if request.method=='GET':
        try:
            _type=request.GET['type']
            status=request.GET['status']
            room=None
            suser=request.user
            if not suser.is_authenticated:
                return JsonResponse({'status': 'User not authenticated'}, status=401)
            user=get_object_or_404(UserInfo,user=suser)
            user=user.id
            search_by_user=False
            if 'room' in request.GET:
                room=request.GET['room']

            if _type=='food':
                if room:
                    orders=Order.objects.filter(user__room=room,status=status)
                    return JsonResponse({'orders':OrderSerializer(orders,many=True).data})
                if search_by_user:
                    orders=Order.objects.filter(user__id=user,status=status)
                    return JsonResponse({'orders':OrderSerializer(orders,many=True).data})
                orders=Order.objects.filter(status=status)
                return JsonResponse({'orders':OrderSerializer(orders,many=True).data})
            
            if _type=='ride':
                if room:
                    rides=Ride.objects.filter(user__room=room,status=status)
                    return JsonResponse({'rides':RideSerializer(rides,many=True).data})
                if search_by_user:
                    rides=Ride.objects.filter(user__id=user,status=status)
                    return JsonResponse({'rides':RideSerializer(rides,many=True).data})
                rides=Ride.objects.filter(status=status)
                return JsonResponse({'rides':RideSerializer(rides,many=True).data})
            
            if _type=='rental':
                if room:
                    rentals=RentalBooking.objects.filter(user__room=room,status=status)
                    return JsonResponse({'rentals':RentalBookingSerializer(rentals,many=True).data})
                if search_by_user:
                    rentals=RentalBooking.objects.filter(user__id=user,status=status)
                    return JsonResponse({'rentals':RentalBookingSerializer(rentals,many=True).data})
                rentals=RentalBooking.objects.filter(status=status)
                return JsonResponse({'rentals':RentalBookingSerializer(rentals,many=True).data})
        except Exception as e:
            return JsonResponse({'error':str(e)},status=404)