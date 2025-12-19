from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import date, datetime
from users.models import Client,Admin, User, Wallet


class Hotel(models.Model):
    title = models.CharField(max_length=128)
    stars = models.DecimalField( #TODO: stars = avg(comments.stars), this means i should add an ability to post comments under a hotel object too
        default=0.0,
        decimal_places=0,
        max_digits=1,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(5.0)
        ]
    )
    image = models.ImageField(upload_to='media/posts/%Y/%m/%d/',null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    views = models.PositiveBigIntegerField(default=0)
    date_founded = models.DateField(default=date.today)
    books_per_year = models.IntegerField(default=0)
    admin = models.OneToOneField(Admin, on_delete=models.SET_NULL, null=True, blank=True, related_name= "hotel")

    def __str__(self): 
        return self.title


class Room(models.Model):
    floor = models.PositiveIntegerField()
    code = models.PositiveIntegerField(default=0)#default = floor*100 + id) #TODO: add logic to set this field(maybe in serializers?)
    is_occupied = models.BooleanField(default = False)
    client = models.OneToOneField(Client, null=True, blank=True, on_delete=models.SET_NULL, related_name= 'room')
    hotel = models.ForeignKey(Hotel, on_delete= models.CASCADE, related_name="rooms")

    def __str__(self): 
        return f'{self.hotel.title}: {self.code}'
    
    
class Booking(models.Model):
    date= models.DateTimeField(auto_now=True)
    price= models.PositiveBigIntegerField()
    client = models.ForeignKey(Wallet, null=True, on_delete=models.SET_NULL, related_name= "payments")

    def __str__(self):
        return self.pk
    

class Achievement(models.Model):
    title = models.CharField(max_length=128)
    user = models.ManyToManyField(User, related_name="achievements")