import datetime
from django.http import JsonResponse
from gig.models.delivery import Delivery
from gig.models.job import Job
from gig.models.worker import Worker
from gig.serializers import DeliverySerializer


def DeliveryDetails(request):
    if request.method == 'POST':
        print('kitaaaa')
        try:
            w=Worker.objects.get(pk=request.POST['worker_id'])
            jobs=Job.objects.filter(worker=w)
            fromdate=datetime.datetime.strptime(request.POST['fromdate'],"%Y-%m-%dT%H:%M:%S.%f")
            todate=datetime.datetime.strptime(request.POST['todate'],"%Y-%m-%dT%H:%M:%S.%f")
            deliveries=Delivery.objects.filter(job__in=jobs,date__range=[fromdate,todate]).order_by('date')
            serializer=DeliverySerializer(deliveries,many=True)
            print(serializer.data)
            return JsonResponse(serializer.data,safe=False, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({'error': 'Something went wrong'}, status=404)
def CommissionDetails(request):
     if request.method == 'POST':
        print('kitaaaa')
        try:
            w=Worker.objects.get(pk=request.POST['worker_id'])
            jobs=Job.objects.filter(worker=w)
            fromdate=datetime.datetime.strptime(request.POST['fromdate'],"%Y-%m-%dT%H:%M:%S.%f")
            todate=datetime.datetime.strptime(request.POST['todate'],"%Y-%m-%dT%H:%M:%S.%f")
            deliveries=Delivery.objects.filter(job__in=jobs,date__range=[fromdate,todate]).order_by('date')
            serializer=DeliverySerializer(deliveries,many=True)
            print(serializer.data)
            return JsonResponse(serializer.data,safe=False, status=200)
        except Exception as e:
            print(e)
            return JsonResponse({'error': 'Something went wrong'}, status=404)