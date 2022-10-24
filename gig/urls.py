from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.cache import never_cache
from .views import *

urlpatterns = [
    path('find-jobs/', never_cache(FindJobs.as_view()), name='find-jobs'),
    path('assign-job/', csrf_exempt(AssignJob.as_view()), name='assign-job'),
    ]