from django.views import View
from django.http import JsonResponse


class GetOTP(View):
    def get(self,request):

        return JsonResponse({"json":"result"})