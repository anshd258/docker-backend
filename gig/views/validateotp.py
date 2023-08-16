from django.http import JsonResponse
from gig.models import Job,Worker,Delivery,Commission
from service.models.order import Order, OrderItem


def ValidateOtp(request):
    if request.method=='POST':
        otp=request.POST['otp']
        uid=request.POST['uid']
        job=Job.objects.get(unique_link=uid)
        print(otp,uid)
        print(job.otp)
        if(job.otp==int(otp)):
            if(job.order.status>4):
                return JsonResponse({'error': 'Job already completed'}, status=404)
            worker=job.worker
            job.order.status=5
            worker.status=1
            worker.deliveries_today+=1
            worker.total_deliveries+=1
            worker.commission_today+=job.commission
            worker.total_commission+=job.commission
            job.save()
            worker.save()
            total=0
            order=Order.objects.get(pk=job.order.id)
            items=OrderItem.objects.filter(order=order)
            for i in items:
                total+=i.total
            Delivery.objects.create(job=job,amount=total,service_type=1)
            Commission.objects.create(job=job,amount=job.commission,service_type=1)
            print(job.worker.total_deliveries)
            return JsonResponse({'status': 'OTP validated'}, status=200)
        else:
            print('fail')
            return JsonResponse({'error': 'OTP not validated'}, status=404)    