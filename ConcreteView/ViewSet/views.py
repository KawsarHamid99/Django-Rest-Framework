from .models import Student
from .serializers import StudentSerializer
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status,viewsets

class StudentViewset(viewsets.ViewSet):
    def list(self,request):
        stu=Student.objects.all() 
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)








from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView


class StudentList(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentRetrieve(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentUpdate(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentDestroy(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class StudentLC(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class Student_RU(RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


class Student_RD(RetrieveDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class Student_RUD(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer