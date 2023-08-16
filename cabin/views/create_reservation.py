import base64
import datetime
import hashlib
import hmac
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from cabin.models import Reservation, PaymentStatus,Property
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
        print(obj)
        location=obj['location']
        price=obj['price']
        loc=Property.objects.filter(name=location).first()
        if loc is None:
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
            print('Rooms are not available')
            return JsonResponse({'status': 'Rooms are not available'}, status=400)
        client = razorpay.Client(auth=(os.environ.get('PUBLIC_KEY'), os.environ.get('SECRET_KEY')))
        user=None
        user=User.objects.filter(email=obj['email_id']).first()
        if user is None:
            name=obj['name'].split(' ')
            fname=name[0]
            lname="undefined"
            if(len(name)==2):lname=name[1]
            if(len(name)==3):lname=name[2]
            user=User.objects.create_user(
                username=obj['name'],
                email=obj['email_id'],
                password=obj['mobile'],
                first_name=fname,
                last_name=lname
            )
            
        obj['user_id']=user.id
        reservation = Reservation.objects.create(
            property=obj["location_id"],
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
            print(data)
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