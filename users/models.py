from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=15, default='+90000000000000')
    avatar = models.ImageField(upload_to='media/avatars/%Y/%m/',null=True, blank=True)
    bio = models.TextField(max_length=256, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    gender = models.BooleanField() #0: Male, 1:Female
    USER_ROLE = (
        ('admin', 'Admin'),
        ('staff', 'Staff'),
        ('client', 'Client'),
    )
    role = models.CharField(choices = USER_ROLE, default= USER_ROLE[2])

    def __str__(self):
        return f"User {self.first_name} {self.last_name}"


class  Admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="admin")
    def __str__(self):
        return f"Admin {self.user.first_name} {self.user.last_name}" 


class Staff (models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="staff")
    hotel = models.ForeignKey('main.Hotel', on_delete=models.SET_NULL, null=True, blank=True)
    def __str__(self):
        return f"Staff {self.user.first_name} {self.user.last_name}" 


class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="client")
    def __str__(self):
        return f"Client {self.user.first_name} {self.user.last_name}"
    


class Wallet(models.Model):
    client = models.OneToOneField(Client, on_delete=models.CASCADE, related_name="wallet")
    balance = models.PositiveBigIntegerField(default= 0)
    is_locked= models.BooleanField(default=False)

    def __str__(self):
        return f"{self.client.user.first_name} {self.client.user.last_name}'s wallet" 



