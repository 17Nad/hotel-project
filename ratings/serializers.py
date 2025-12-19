from rest_framework import serializers
from datetime import date
from rest_framework.validators import ValidationError
from main.models import Hotel, Room
from ratings.models import Post, Comment, Reply


class ReplySrz(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = "__all__"


class CommentSrz(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
    replies = ReplySrz(many=True, read_only=True)


class PostSrz(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__" 
    comments = CommentSrz(many=True, read_only=True)