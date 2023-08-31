from django.views import View
from django.http import JsonResponse
from user.otp_generation import GenerateOTP
from django.views.decorators.csrf import csrf_exempt

class GetOTP:

    def getotp(phone):
        otp = GenerateOTP()
        try:
            otp=otp.get_otp(phone)['otp']
            return otp
        except Exception as e:
            return 0
