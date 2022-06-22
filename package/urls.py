from django.urls import path
from package.views import CreatePackage

urlpatterns = [
    path('create-package/', CreatePackage.as_view(), name='create-package')
]
