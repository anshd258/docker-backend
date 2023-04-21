import datetime
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

class CreateReservation(View):
    def get(self, request):
        pass

    @csrf_exempt
    def post(self, request):
        obj = json.loads(request.body)
        loc=Location.objects.filter(name=obj['location']).first()
        obj['location_id']=loc.id
        # if not CalculateAvailability(
        #         obj['location_id'],
        #         obj['rooms'],
        #         obj['checkin'],
        #         obj['checkout']
        #         ):
        #     return JsonResponse({'status': 'Rooms are not available'})
        client = razorpay.Client(auth=(os.environ.get('PUBLIC_KEY'), os.environ.get('SECRET_KEY')))
        user=User.objects.filter(first_name=obj['first_name']).first()
        obj['user_id']=user.id
        reservation = Reservation.objects.create(
            location_id=obj["location_id"],
            user_id=obj["user_id"],
            price=obj["price"],
            adults=obj["adults"],
            children=obj["children"],
            checkin=pytz.utc.localize(datetime.datetime.strptime(obj['checkin'], '%Y-%m-%d %H:%M:%S')),
            checkout=pytz.utc.localize(datetime.datetime.strptime(obj['checkout'], '%Y-%m-%d %H:%M:%S')),
            rooms=obj["rooms"]
        )
        amount=int(obj["price"])
        razor_payment = client.order.create({"amount": int(amount) * 100, 
                                   "currency": "INR", 
                                   "payment_capture": "1"})
        payment = PaymentStatus.objects.create(
            payment_ref_id=razor_payment["id"],
            reservation_id=reservation.id,
            amount=obj["price"]
        )
        print(PaymentStatusSerializer(payment, many=False).data)
        response=JsonResponse({'payment_status':PaymentStatusSerializer(payment, many=False).data})
        response.status_code=200
        return response
    def success(request):
        res = json.loads(request.data["response"])

        ord_id = ""
        raz_pay_id = ""
        raz_signature = ""
        for key in res.keys():
            if key == 'razorpay_order_id':
                ord_id = res[key]
            elif key == 'razorpay_payment_id':
                raz_pay_id = res[key]
            elif key == 'razorpay_signature':
                raz_signature = res[key]

        payment=PaymentStatus.objects.filter(payment_ref_id=ord_id).first()
        data = {
        'razorpay_order_id': ord_id,
        'razorpay_payment_id': raz_pay_id,
        'razorpay_signature': raz_signature
        }
        client = razorpay.Client(auth=(os.environ.get('PUBLIC_KEY'), os.environ.get('SECRET_KEY')))
        check = client.utility.verify_payment_signature(data)

        if check is not None:
            print("Redirect to error url or error page")
            return JsonResponse({'error': 'Something went wrong'})
        payment.status = True
        payment.save()
        res_data = {
        'message': 'payment successfully received!'
        }

        return JsonResponse(res_data)
