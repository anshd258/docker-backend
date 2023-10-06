import os
from rest_framework.views import APIView
import razorpay
from django.conf import settings
from service.models.order import Order
from django.http import JsonResponse
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
class OrderPayment(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        client=razorpay.Client(auth=(os.environ.get('PUBLIC_KEY'), os.environ.get('SECRET_KEY')))
        data = request.data
        order_id=data['order_id']
        amount=Order.objects.get(id=order_id).total
        order_currency = 'INR'
        payment = client.order.create(dict(amount=amount, currency=order_currency))
        return JsonResponse(payment)
    
class OrderVerify(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        client=razorpay.Client(auth=(os.environ.get('PUBLIC_KEY'), os.environ.get('SECRET_KEY')))
        data = request.data
        order_id=data['order_id']
        payment_id=data['payment_id']
        signature=data['signature']
        data = {
            'razorpay_order_id': order_id,
            'razorpay_payment_id': payment_id,
            'razorpay_signature': signature
            }
        try:
            client.utility.verify_payment_signature(data)
            return JsonResponse({'status':'success'})
        except Exception as e:
            print(e)
            return JsonResponse({'status':'failed'})

    
    