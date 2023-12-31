from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=12)
    username=models.CharField(max_length=100,null=True)
    room=models.CharField(max_length=20,null=True)
    property_id=models.IntegerField(null=True)
    def __str__(self):
        return str(self.user.username) + ", " + str(self.contact)


# @receiver(post_save, sender=settings.AUTH_USER_MODEL)
# def create_auth_token(sender, instance=None, created=False, **kwargs):
#     if created:
#         Token.objects.create(user=instance)
