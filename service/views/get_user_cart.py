from django.http import JsonResponse
from user.models import UserInfo
from service.models import Order
from service.serializers import OrderSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

class GetUserCart(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        try:
            su=request.user
            user=UserInfo.objects.get(user=su)
            status=request.GET.get('status')
            orders=Order.objects.filter(user=user,status=status)
            orders=OrderSerializer(orders,many=True).data
            return JsonResponse({'cart':orders},status=200)
        except Exception as e:
            print(e)
            return JsonResponse({'status':'error'},status=400)