from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from main.models import Hotel
from users.models import User


class Post(models.Model): #only hotel admins can upload posts.
    title = models.CharField(max_length=128)
    media = models.ImageField(upload_to='media/posts/%Y/%m/%d/', null=True, blank=True)
    caption = models.TextField(null=True, blank=True)
    comments_are_allowed = models.BooleanField(default=True)
    comments_count = models.IntegerField(default= 0)
    views= models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    date_posted = models.DateTimeField(auto_now=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.SET_NULL, null=True, blank=True, related_name="rating")

    def __str__(self):
        return f"{self.hotel.title} posted: {self.title}"
  


class Comment(models.Model): #all users(admins, hotel staff, and clients) can post comments on posts, or on hotel's profiles 
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
    post = models.ForeignKey(Post, on_delete = models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="comments")

    def __str__(self):
        return f"{self.user.first_name} commented: {self.message}"
    

class Reply(models.Model):
    message = models.TextField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name="replies")
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL, related_name="replies")

    def __str__(self):
        return f"{self.user.first_name} replied: {self.message}"