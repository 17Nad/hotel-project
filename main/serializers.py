from rest_framework import serializers
from datetime import date
from rest_framework.validators import ValidationError
from main.models import Hotel, Room
from ratings.models import Post, Comment, Reply
from ratings.serializers import CommentSrz


class HotelSrz(serializers.ModelSerializer):
    class Meta:
        model= Hotel
        fields =  "__all__"
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    comments = CommentSrz(many=True, read_only=True)


