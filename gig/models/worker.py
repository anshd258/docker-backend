from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone
from user.models import UserInfo
from service.models import Location


class Worker(models.Model):
    class Status(models.IntegerChoices):
        AVAILABLE=1
        ASSIGNED=2
        ON_THE_WAY=3
    user_info = models.OneToOneField(UserInfo, on_delete=models.CASCADE)
    service_areas = models.ManyToManyField(Location)
    earnings = models.DecimalField(decimal_places=2, default=0.0, max_digits=8)
    rating = models.DecimalField(decimal_places=2, default=0.0, max_digits=8)
    status = models.PositiveSmallIntegerField(choices=Status.choices, default=Status.AVAILABLE)
    deliveries_today=models.IntegerField(default=0)
    total_deliveries=models.IntegerField(default=0)
    commission_today=models.DecimalField(null=True,decimal_places=2, default=0.0, max_digits=8)
    total_commission=models.DecimalField(null=True,decimal_places=2, default=0.0, max_digits=8)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.user_info.user.username + ", " + self.user_info.contact
    

@receiver(pre_save, sender=Worker)
def reset_deliveries_today(sender, instance, **kwargs):
    today = timezone.now().date()
    if instance.id:
        previous_instance = Worker.objects.get(id=instance.id)
        if previous_instance.updated_at.date() < today <= instance.updated_at.date():
            instance.deliveries_today = 0