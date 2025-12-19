from django.urls import path, include
from main.views import *
from rest_framework.routers import DefaultRouter

app_name= 'main'
router = DefaultRouter()

router.register(r"home", HomeViewSet, basename="HomePage")

urlpatterns = [
    path("api/", include(router.urls))
]
