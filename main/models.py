from django.db import models
from datetime import date, datetime
from users.models import Client, User, Wallet


class Hotel(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    date_founded = models.DateField(default=date.today)
    books_per_year = models.IntegerField(default=0)

    def __str__(self): 
        return self.title


class Room(models.Model):
    floor = models.PositiveIntegerField()
    code = models.PositiveIntegerField(null = True)#default = floor*100 + id) #FIXME: remove nullabality later
    is_occupied = models.BooleanField(default = False)
    client = models.OneToOneField(Client, null=True, blank=True, on_delete=models.SET_NULL, related_name= 'room')
    hotel = models.ForeignKey(Hotel, on_delete= models.CASCADE, related_name="rooms")

    def __str__(self): 
        return self.code
    
    
class Booking(models.Model):
    date= models.DateTimeField(auto_now=True)
    price= models.PositiveBigIntegerField()
    client = models.ForeignKey(Wallet, null=True, on_delete=models.SET_NULL, related_name= "payments")

    def __str__(self):
        return self.pk
    

class Achievement(models.Model):
    title = models.CharField(max_length=128)
    user = models.ManyToManyField(User, related_name="achievements")