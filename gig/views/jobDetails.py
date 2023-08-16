from django.http import  JsonResponse
from django.shortcuts import render
from gig.models.job import Job
from gig.serializers import JobSerializer

def jobDetails(request, unique_link):
    if request.method == 'POST':
        pass
    print(unique_link)
    try:
       job=Job.objects.get(unique_link=unique_link)
       if job is not None: 
        # deserialize the job object and send as json
        if(job.order.status>4):
            return JsonResponse({'error': 'Job already accepted'}, status=404)
        job=JobSerializer(job,many=False)
        return JsonResponse(job.data)
    except Job.DoesNotExist:
        return JsonResponse({'error': 'Job does not exist'}, status=404)