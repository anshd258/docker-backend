from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from . import views
from .views import *

urlpatterns = [
    path('find-jobs/', never_cache(FindJobs.as_view()), name='find-jobs'),
    path('assign-job/', csrf_exempt(AssignJob.as_view()), name='assign-job'),
    path('find-workers/', never_cache(FindWorkers.as_view()), name='find-workers'),
    path('jobdetails/<str:unique_link>/',(jobDetails), name='jobdetails'),
    path('acceptjob/<str:unique_link>/',csrf_exempt(acceptJob), name='acceptjob'),
    path('validateotp/',csrf_exempt(ValidateOtp), name='validateotp'),
    path('workersummary/',csrf_exempt(WorkerSummary), name='workersummary'),
    path('deliverydetails/',csrf_exempt(DeliveryDetails), name='deliverydetails'),
    path('commissiondetails/',csrf_exempt(CommissionDetails), name='commissiondetails'),
]