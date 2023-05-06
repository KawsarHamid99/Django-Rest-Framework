from django.shortcuts import render
from filterapp.models import Student
from filterapp.serializers import StudentSerializer

from rest_framework import viewsets
# Create your views here.
from rest_framework.generics import ListAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated 

from django_filters.rest_framework import DjangoFilterBackend

class GenericFilter(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    # authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]
    filter_backends=[DjangoFilterBackend]
    filterset_fields=["name"]

class GenericLIST(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    # authentication_classes=[SessionAuthentication]
    # permission_classes=[IsAuthenticated]
    filter_backends=[DjangoFilterBackend]
    filterset_fields=["name"]

