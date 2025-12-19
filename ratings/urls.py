from django.urls import path, include
from ratings.views import *
from rest_framework.routers import DefaultRouter

app_name= 'ratings'
router = DefaultRouter()

# router.register(r"hotel", HotelPostsViewSet, basename="hotelPosts")

urlpatterns = [
    path("<int:pk>/", HotelPostsAPIView.as_view(), name="hotelPosts"),
    path("<int:hotel_pk>/post/<int:post_pk>/", PostCommentsAPIView.as_view(), name="postComments"),
    path("api/", include(router.urls)),
]
