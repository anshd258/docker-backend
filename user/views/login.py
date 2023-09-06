
import json
from django.http import JsonResponse
from rest_framework.views import APIView
from user.models.user_info import UserInfo
from user.views.get_otp import GetOTP
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class Login(APIView):
    def get(self, request):
        phone=request.GET.get('phone')
        user=UserInfo.objects.filter(contact=phone).first()
        if user is None:
            f=User.objects.create_user(username=phone,password=phone)
            user=UserInfo.objects.create(user=f,contact=phone)
        otp=GetOTP.getotp(phone)
        if otp==0:
            return JsonResponse({'status': 'OTP not sent'}, status=400)
        user.otp=otp
        user.save()
        return JsonResponse({'status': 'OTP sent successfully'}, status=200)
    
    def post(self, request):
        body=json.loads(request.body)
        phone=body['phone']
        name=body['username']
        otp=body['otp']
        room=body['room']
        user=UserInfo.objects.filter(contact=phone).first()
        if user is None:
            return JsonResponse({'status': 'User not found'}, status=400)
        if str(otp)==user.otp:
            user.otp=None
            if user.username is None:
                user.username=name
                user.save()
            if len(room)>0:
                user.room=room
                user.save()
            suser=User.objects.filter(id=user.user_id).first()
            refresh = RefreshToken.for_user(suser)
            return JsonResponse({'refresh': str(refresh),'access': str(refresh.access_token),}, status=200)
        return JsonResponse({'status': 'Login failed'}, status=400)
        