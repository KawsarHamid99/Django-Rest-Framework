from django.shortcuts import render,HttpResponse
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter,OrderingFilter
# Create your views here.
def searchview(request):
    return HttpResponse("hello world")

class Studentviewsets(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    #search
    #filter_backends=[SearchFilter]
    #search_fields=['name',"id"]
    #search_fields=["^name"]

    #ordering
    filter_backends=[OrderingFilter]
    ordering_fields=['dept']