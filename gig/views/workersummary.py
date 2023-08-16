from django.http import JsonResponse
from gig.models.worker import Worker


def WorkerSummary(request):
    if request.method=='POST':
        worker=Worker.objects.get(pk=request.POST['worker_id'])
        if worker is not None:
            data={}
            data['totaldel']=worker.total_deliveries
            data['todaydel']=worker.deliveries_today
            data['totalcom']=worker.total_commission
            data['todaycom']=worker.commission_today
            print(data)
            return JsonResponse(data, status=200)
        else :return JsonResponse({'error': 'Worker not found'}, status=404)