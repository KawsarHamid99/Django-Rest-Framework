from django.shortcuts import render
from rest_framework.authentication import SessionAuthentication,BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.

from .models import Student
from .serializeras import StudentSerializer
from rest_framework.viewsets import ModelViewSet

class StudentClass(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAuthenticated]
