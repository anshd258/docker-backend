from django.http import JsonResponse
from gig.models.job import Job
from gig.models.worker import Worker
from gig.views import assign_job


def acceptJob(request,unique_link):
    if request.method=='POST':
        print('herrrrrrrrrrrr')
        job=Job.objects.get(unique_link=unique_link)
        print(request.POST['worker_id'])
        worker=Worker.objects.get(id=request.POST['worker_id'])
        if(job.worker is not None and job.worker.id!=worker.id):
            return JsonResponse({'error': 'Job already assigned'}, status=404)
        elif (job.worker is not None and job.worker.id==worker.id):
            return JsonResponse({'error': 'Job already accepted'}, status=200)
        if assign_job.AssignJob.assign(None,job.id, worker.user_info.contact):
            return JsonResponse({'status': 'Job assigned'}, status=200)
        else:
            return JsonResponse({'error': 'Job not assigned'}, status=404)
