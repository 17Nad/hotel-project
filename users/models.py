from django.db import models
from django.contrib.auth.models import AbstractUser
from main.models import *


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, default='+90000000000000')
    avatar = models.ImageField(upload_to='media/avatars/%Y/%m/',null=True, blank=True)
    age=models.PositiveIntegerField()
    gender = models.BooleanField()
    USER_ROLE = (
        (0, 'Admin'),
        (1, 'Staff'),
        (2, 'Client'),
    )
    role = models.CharField(choices = USER_ROLE, default= USER_ROLE[2])

    def __str__(self):
        return f"User {self.user.first_name} {self.user.last_name}"


class  Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="Admin")
    def __str__(self):
        return f"Admin {self.user.first_name} {self.user.last_name}" 


class Staff (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="staff")
    def __str__(self):
        return f"Staff {self.user.first_name} {self.user.last_name}" 


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="client")
    def __str__(self):
        return f"Client {self.user.first_name} {self.user.last_name}"
    


class Wallet(models.Model):
    wallet = models.OneToOneField(Client, on_delete=models.CASCADE, related_name="wallet")
    balance = models.PositiveBigIntegerField(default= 0)
    is_locked= models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}'s wallet" 



