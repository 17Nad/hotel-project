from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from django.shortcuts import get_object_or_404
from main.models import Hotel
from ratings.models import Post, Comment, Reply
from ratings.serializers import *


#BUG: bullshit
class HotelPostsAPIView(APIView):
    def get(self, request, pk=None):
        hotel = get_object_or_404(Hotel, pk)
        queryset = Post.objects.filter(hotel=hotel)
        serializer = PostSrz(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class PostCommentsAPIView(APIView):
    def get(self, request, hotel_pk, post_pk):
        post = get_object_or_404(Post, pk=post_pk, hotel=hotel_pk)
        comments = Comment.objects.filter(post=post)
        # Optionally, include replies in the response
        data = []
        for comment in comments:
            comment_data = CommentSrz(comment).data
            replies = Reply.objects.filter(comment=comment)
            comment_data['replies'] = ReplySrz(replies, many=True).data
            data.append(comment_data)
        return Response(data, status=status.HTTP_200_OK)










































#TODO: they are not tested well
# class HotelPostsViewSet(ModelViewSet):
#     # queryset = Post.objects.filter(hotel=pk):
#     serializer_class = PostSrz
#     permission_classes = [IsAuthenticatedOrReadOnly]
    

#     def list(self, request, pk):
#         if not get_object_or_404(Hotel, id = pk):
#             return Response({"error": "Hotel not found."}, status=status.HTTP_404_NOT_FOUND)
#         queryset = Post.objects.filter(hotel=pk)
#         serializer = PostSrz(queryset, many=True) #BUG: it returns a post with null fields for some reason
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def retrieve(self, request, pk=None, id=None):
#         if not get_object_or_404(Hotel, id = pk) and not get_object_or_404(Post, id = id):
#             return Response({"error": "Post or Hotel not found."}, status=status.HTTP_404_NOT_FOUND)
#         serializer = PostSrz()
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def create (self, request, pk):
#         if not get_object_or_404(Post, id= pk):
#             return Response({"error": "Post not found."}, status=status.HTTP_404_NOT_FOUND)
#         serializer = CommentSrz(data=request.data)
#         if serializer.is_valid() and serializer.data['post'] == pk:
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         else:
#             return Response ({"error": "Invalid data."}, status=status.HTTP_400_BAD_REQUEST)
            
