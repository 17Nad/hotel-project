from rest_framework import serializers
from datetime import date
from rest_framework.validators import ValidationError
from main.models import Hotel, Room
from ratings.models import Post

class HotelSrz(serializers.ModelSerializer):
    class Meta:
        model= Hotel
        fields =  "__all__"


class PostSrz(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__" 