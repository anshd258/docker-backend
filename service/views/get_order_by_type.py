import json
from django.http import JsonResponse
from ..models import *
from ..serializers import *

def GetOrderByType(request):
    if request.method=='GET':
        try:
            _type=request.GET['type']
            status=request.GET['status']
            room=None
            user=None
            if 'room' in request.GET:
                room=request.GET['room']
            if 'user' in request.GET:
                user=request.GET['user']

            if _type=='food':
                if room:
                    orders=Order.objects.filter(user__room=room,status=status)
                    return JsonResponse({'orders':OrderSerializer(orders,many=True).data})
                if user:
                    orders=Order.objects.filter(user__id=user,status=status)
                    return JsonResponse({'orders':OrderSerializer(orders,many=True).data})
                orders=Order.objects.filter(status=status)
                return JsonResponse({'orders':OrderSerializer(orders,many=True).data})
            
            if _type=='ride':
                if room:
                    rides=Ride.objects.filter(user__room=room,status=status)
                    return JsonResponse({'rides':RideSerializer(rides,many=True).data})
                if user:
                    rides=Ride.objects.filter(user__id=user,status=status)
                    return JsonResponse({'rides':RideSerializer(rides,many=True).data})
                rides=Ride.objects.filter(status=status)
                return JsonResponse({'rides':RideSerializer(rides,many=True).data})
            
            if _type=='rental':
                if room:
                    rentals=RentalBooking.objects.filter(user__room=room,status=status)
                    return JsonResponse({'rentals':RentalBookingSerializer(rentals,many=True).data})
                if user:
                    rentals=RentalBooking.objects.filter(user__id=user,status=status)
                    return JsonResponse({'rentals':RentalBookingSerializer(rentals,many=True).data})
                rentals=RentalBooking.objects.filter(status=status)
                return JsonResponse({'rentals':RentalBookingSerializer(rentals,many=True).data})
        except Exception as e:
            return JsonResponse({'error':str(e)},status=404)