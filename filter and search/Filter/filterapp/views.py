from django.shortcuts import render,HttpResponse
from .serializers import StudentSerializer
from .models import Student
from rest_framework import viewsets

class StudentViewset(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get_queryset(self):
        user=self.request.user
        return Student.objects.filter(name=user)

# Create your views here.

def home(request):
    return HttpResponse("hello world")
