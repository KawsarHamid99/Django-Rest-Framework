from django.shortcuts import render,HttpResponse
from .models import Student

from django.http import JsonResponse
from .serializer import StudentSerializer
from rest_framework.generics import ListCreateAPIView

from rest_framework import viewsets

class StudentViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


