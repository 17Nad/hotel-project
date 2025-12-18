from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from main.models import Hotel
from users.models import User


# Source - https://stackoverflow.com/a
# Posted by San4ez
# Retrieved 2025-12-18, License - CC BY-SA 3.0
# class MinMaxFloat(models.FloatField):
#     def __init__(self, min_value=None, max_value=None, *args, **kwargs):
#         self.min_value, self.max_value = min_value, max_value
#         super(MinMaxFloat, self).__init__(*args, **kwargs)

#     def formfield(self, **kwargs):
#         defaults = {'min_value': self.min_value, 'max_value' : self.max_value}
#         defaults.update(kwargs)
#         return super(MinMaxFloat, self).formfield(**defaults)


class Rating(models.Model): #this is supposed to act like a plog post, to be the main page for a hotel and show its information
    stars = models.FloatField(
        default=0.0,
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(5.0)
        ]
    )
    image = models.ImageField(upload_to='media/hotels/%Y/%m/',null=True, blank=True)
    description = models.TextField()
    views = models.PositiveBigIntegerField(default=0)
    comments_count = models.IntegerField(default= 0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    hotel = models.OneToOneField(Hotel, on_delete=models.CASCADE, related_name="rating")

    def __str__(self):
        return f"{self.hotel.title}'s ratings"
  


class Comment(models.Model):
    stars = models.PositiveSmallIntegerField(
        default=0,
        validators=[
            MinValueValidator(0),  
            MaxValueValidator(5)
        ]
    )
    message = models.TextField()
    views = models.PositiveIntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="comments")