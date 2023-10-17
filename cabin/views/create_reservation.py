import datetime
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from cabin.availability.calculate_availability import CalculateAvailability_fromRoom
from cabin.models import Reservation, PaymentStatus,Property,Room
from user.models import UserInfo
from cabin.availability import CalculateAvailability
import json
import os
import razorpay
from django.views.decorators.csrf import csrf_exempt
import pytz
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
class CreateReservation(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    @csrf_exempt
    def post(self, request):
        obj = json.loads(request.body)
        propertyid=obj['propertyid']
        roomid=obj['roomid']
        rooms=obj['rooms']
        chkin=pytz.utc.localize(datetime.datetime.strptime(obj['checkin'], '%Y-%m-%d %H:%M:%S'))
        chkout=pytz.utc.localize(datetime.datetime.strptime(obj['checkout'], '%Y-%m-%d %H:%M:%S'))
        if not CalculateAvailability_fromRoom(
                roomid,
                rooms,
                chkin,
                chkout
                ):
            print('Rooms are not available')
            return JsonResponse({'status': 'Rooms are not available'}, status=400)
        room_instance=get_object_or_404(Room,id=roomid)
        price=room_instance.price*rooms
        client = razorpay.Client(auth=(os.environ.get('PUBLIC_KEY'), os.environ.get('SECRET_KEY')))
        su=request.user
        user=UserInfo.objects.filter(user=su).first()
        reservation = Reservation.objects.create(
            room=room_instance,
            user=user,
            price=int(price),
            adults=obj["adults"],
            children=obj["children"],
            checkin=chkin,
            checkout=chkout,
            roomsbooked=rooms,
            property_id=propertyid
        )
        amount=int(price)
        razor_payment = client.order.create({"amount": int(amount) * 100, 
                                   "currency": "INR", 
                                   "payment_capture": "1"})
        payment = PaymentStatus.objects.create(
            payment_ref_id=razor_payment["id"],
            reservation_id=reservation.id,
            amount=price
        )
        response=JsonResponse({'order_id':razor_payment['id']})
        response.status_code=200
        return response
    
    @api_view(['POST'])
    def success(request):
        res=json.loads(request.body)
        order_id = res['orderId']
        payment_id = res['razorpay_payment_id']
        signature= res['razorpay_signature']
        client = razorpay.Client(auth=(os.environ.get('PUBLIC_KEY'), os.environ.get('SECRET_KEY')))
        try:
            data = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
            }
            client.utility.verify_payment_signature(data)
            Payment=PaymentStatus.objects.filter(payment_ref_id=order_id).first()
            Payment.status=True
            Payment.save()
            return JsonResponse({'status':'Payment Successful'})
        except Exception as e:
            print(e)
            resp=JsonResponse({'status':'Payment Failed'})
            resp.status_code=500
            return resp

