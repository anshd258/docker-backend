
import json
from django.http import JsonResponse
from rest_framework.views import APIView
from user.models.user_info import UserInfo
from user.otp_generation import GenerateOTP
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken

class Login(APIView):
    def get(self, request):
        phone=request.GET.get('phone')
        obj=GenerateOTP()
        jwt=obj.get_otp(phone)
        if jwt is None:
            return JsonResponse({'status': 'OTP not sent'}, status=400)
        return JsonResponse({"jwt":jwt}, status=200)
    
    def post(self, request):
        try:
            jwt=request.headers.get('jwt')
            body=json.loads(request.body)
            otp=body['otp']
            verification=GenerateOTP.verify_token(jwt,otp)
            if verification is False:
                return JsonResponse({'status': 'OTP verification failed'}, status=400)
            phone=body['phone']
            new_user=False
            user=UserInfo.objects.filter(contact=phone).first()
            if user is None:
                u=User.objects.create_user(username=phone, password=phone)
                user=UserInfo.objects.create(user=u, contact=phone)
                new_user=True
            suser=user.user
            refresh = RefreshToken.for_user(suser)
            return JsonResponse({'refresh': str(refresh),'access': str(refresh.access_token),'new_user':new_user}, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({'status': 'Login failed'}, status=400)

        