from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    contact = models.CharField(max_length=12)

    def __str__(self):
        return str(self.user.username) + ", " + str(self.contact)
