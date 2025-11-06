from django.shortcuts import render
from rest_framework import generics
from.models import InformationsModel
from .serializers import InformationSerializer
from drf_spectacular.utils import extend_schema
# Create your views here.

class ListCreateInformation(generics.ListCreateAPIView):
    queryset = InformationsModel.objects.all()
    serializer_class = InformationSerializer

class RetrieveUpdateDestroyInformation(generics.RetrieveUpdateDestroyAPIView):
    queryset = InformationsModel.objects.all()
    serializer_class = InformationSerializer