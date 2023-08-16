from django.http import JsonResponse
from django.views import View
from package.package_builder import PackageBuilder


class CreatePackage(View):

    def get(self, request):
        try:
            package = PackageBuilder(int(request.GET["duration"]), int(request.GET["guests"]), request.GET["preferences"])
            return JsonResponse({"status": package.calculate()})
        except Exception as e:
            return JsonResponse({"status": str(e)}, status=404)