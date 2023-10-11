import json
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.db.models import Q
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
            status=None
            room=None
            suser=request.user
            if not suser.is_authenticated:
                return JsonResponse({'status': 'User not authenticated'}, status=401)
            user=get_object_or_404(UserInfo,user=suser)
            user=user.id
            search_by_user=request.GET['search_by_user']
            queries={}
            if 'room' in request.GET:
                room=request.GET['room']
                queries['user__room']=room
            if 'status' in request.GET:
                status=request.GET['status']
                queries['status']=status
            if search_by_user==1:
                queries['user__id']=user
            q_objects=Q(**queries)
            if _type=='food':
                orders=Order.objects.filter(q_objects)
                return JsonResponse({'orders':OrderSerializer(orders,many=True).data})
            
            if _type=='ride':
                rides=Ride.objects.filter(q_objects)
                return JsonResponse({'rides':RideSerializer(rides,many=True).data})
            
            if _type=='rental':
                rentals=RentalBooking.objects.filter(q_objects)
                return JsonResponse({'rentals':RentalBookingSerializer(rentals,many=True).data})
        except Exception as e:
            return JsonResponse({'error':str(e)},status=404)