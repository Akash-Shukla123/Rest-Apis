from django.shortcuts import render
from rest_framework import viewsets
from . models import task
from .serializers import taskserializer

class taskview(viewsets.ModelViewSet):
    queryset = task.objects.all()
    serializer_class= taskserializer