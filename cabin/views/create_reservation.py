import base64
import datetime
import hashlib
import hmac
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from cabin.models import Reservation, PaymentStatus,Location
from user.models import User
from cabin.availability import CalculateAvailability
from cabin.serializers import PaymentStatusSerializer,ReservationSerializer
import json
import os
import razorpay
from django.views.decorators.csrf import csrf_exempt
import pytz
from rest_framework.decorators import api_view

class CreateReservation(View):
    def get(self, request):
        pass

    @csrf_exempt
    def post(self, request):
        obj = json.loads(request.body)
        location=obj['location']
        price=obj['price']
        try:
            loc=Location.objects.filter(name=location).first()
        except:
            return JsonResponse({'status': 'Location not found'})
    
        obj['location_id']=loc.id
        chkin=pytz.utc.localize(datetime.datetime.strptime(obj['checkin'], '%Y-%m-%d %H:%M:%S'))
        chkout=pytz.utc.localize(datetime.datetime.strptime(obj['checkout'], '%Y-%m-%d %H:%M:%S'))
        if not CalculateAvailability(
                obj['location_id'],
                obj['rooms'],
                chkin,
                chkout
                ):
            return JsonResponse({'status': 'Rooms are not available'})
        client = razorpay.Client(auth=(os.environ.get('PUBLIC_KEY'), os.environ.get('SECRET_KEY')))
        user=User.objects.filter(email=obj['email_id']).first()
        obj['user_id']=user.id
        reservation = Reservation.objects.create(
            location_id=obj["location_id"],
            user_id=obj["user_id"],
            price=int(price),
            adults=obj["adults"],
            children=obj["children"],
            checkin=chkin,
            checkout=chkout,
            rooms=obj["rooms"]
        )
        amount=int(price)
        razor_payment = client.order.create({"amount": int(amount) * 100, 
                                   "currency": "INR", 
                                   "payment_capture": "1"})
        payment = PaymentStatus.objects.create(
            payment_ref_id=razor_payment["id"],
            reservation_id=reservation.id,
            amount=obj["price"]
        )
        response=JsonResponse({'order_id':razor_payment['id']})
        response.status_code=200
        return response
    
    @api_view(['POST'])
    def success(request):
        res=json.loads(request.body)
        order_id = res['orderId']
        payment_id = res['paymentId']
        signature= res['signature']
        client = razorpay.Client(auth=(os.environ.get('PUBLIC_KEY'), os.environ.get('SECRET_KEY')))
        try:
            data = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
            }
            client.utility.verify_payment_signature(data)
            return JsonResponse({'status':'Payment Successful'})
        except:
            resp=JsonResponse({'status':'Payment Failed'})
            resp.status_code=500
            return resp