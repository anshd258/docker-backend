from django.http import JsonResponse
from django.views import View
from service.catalog import GenerateCatalog
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
class GetMenu(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request) -> JsonResponse:
        catalog = GenerateCatalog()
        try:
            return JsonResponse({"catalog": catalog.build_catalog(request.GET['location'])})
        except Exception as e:
            return JsonResponse({"error": str(e)})

    def post(self):
        pass
