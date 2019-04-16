from django.shortcuts import render
from rest_framework import viewsets
from .models import student
from .serializers import studentserializer,userserializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model

class studentview(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset=student.objects.all()
    serializer_class=studentserializer

    
class createuserView(CreateAPIView):
    model=get_user_model()
    permission_classes = (AllowAny,)
    serializer_class= userserializer