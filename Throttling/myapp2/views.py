from django.shortcuts import render
from myapp.models import Teacher
from myapp.serializers import TeacherSerilaizer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView
# Create your views here.
from rest_framework import viewsets
from rest_framework.throttling import ScopedRateThrottle

class teacherList(ListAPIView):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerilaizer

    throttle_classes=[ScopedRateThrottle]
    throttle_scope='viewstu'


class teacherRUD(RetrieveUpdateDestroyAPIView):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerilaizer
    throttle_classes=[ScopedRateThrottle]
    throttle_scope='rudstu'




class teacherCreate(CreateAPIView):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerilaizer


class teacherRetrieve(RetrieveAPIView):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerilaizer

class teacherDestroy(DestroyAPIView):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerilaizer

class teacherUpdate(UpdateAPIView):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerilaizer

class teacherListCreate(ListCreateAPIView):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerilaizer



class Teacherviewset(viewsets.ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerilaizer
