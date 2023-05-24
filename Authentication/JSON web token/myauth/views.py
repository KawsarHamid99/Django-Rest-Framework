from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .serializer import StudentSerializer
from .models import Student
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class StudentViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    #authentication_classes=[SessionAuthentication]
    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

