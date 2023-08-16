from django.views import View
from django.http import JsonResponse
from user.otp_generation import GenerateOTP


class GetOTP(View):
    def get(self, request):
        otp = GenerateOTP()
        try:
            return JsonResponse(otp.get_otp(request.GET['phone']))
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)
