from django.db import models
from datetime import date, datetime
from users.models import Client


class Hotel(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    date_founded = models.DateField(default=date.today)
    # ratings = models.ForeignKey(Rating)

    def __str__(self): 
        return self.title


class Room(models.Model):
    floor = models.PositiveIntegerField()
    code = models.PositiveIntegerField(null = True)#default = floor*100 + id) #FIXME: remove nullabality later
    is_occupied = models.BooleanField(default = False)
    client = models.OneToOneField(Client, null=True, blank=True, on_delete=models.SET_NULL, related_name= 'room')
    hotel = models.ForeignKey(Hotel, on_delete= models.CASCADE)

    def __str__(self): 
        return self.code