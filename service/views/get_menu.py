from django.http import JsonResponse
from django.views import View
from service.catalog import GenerateCatalog


class GetMenu(View):
    def get(self, request):
        catalog = GenerateCatalog()
        return JsonResponse({"catalog": catalog.build_catalog("LocationA")})

    def post(self):
        pass
