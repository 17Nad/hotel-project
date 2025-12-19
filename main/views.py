from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from main.serializers import *
from main.models import Hotel
from ratings.models import Post


class HomeViewSet(ModelViewSet):
    permission_classes= [AllowAny]
    serializer_class = HotelSrz
    http_method_names = ['get']

    def list(self, request):
        """the home page. HotelPages of top hotels are listed + some information about the user's account if they're logged in (f authentication for now)"""
        #TODO: add user's info here after auth settings are done
        queryset = Hotel.objects.all()
        serializer= HotelSrz(queryset, many=True, read_only=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """this shows up when user clicks on a Page object"""
        queryset = get_object_or_404(Hotel, id=pk)
        serializer= HotelSrz(queryset, read_only=True)
        return Response (serializer.data, status=status.HTTP_200_OK)


#class 
