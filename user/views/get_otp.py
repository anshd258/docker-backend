from django.views import View
from django.http import JsonResponse
from user.otp_generation import GenerateOTP


class GetOTP(View):
    def get(self, request):
        otp = GenerateOTP()
        return JsonResponse(otp.get_otp('7009198527'))

    def post(self):
        pass