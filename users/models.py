from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import *


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, default='+90000000000000')
    avatar = models.ImageField(upload_to='media/avatar/%Y/%m/',null=True, blank=True)
    USER_ROLE = (
        (0, 'Admin'),
        (1, 'Staff'),
        (2, 'Client'),
    )
    role = models.CharField(choices = USER_ROLE, default= USER_ROLE[2])


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="client")
    
    def __str__(self):
        return self.user.first_name 