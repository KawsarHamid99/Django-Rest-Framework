from django.shortcuts import render,HttpResponse
from .models import Teacher
from .serializers import TeacherSerilaizer
from rest_framework import viewsets

from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
from .throttling import JsckRateThrottle


class StudentModelViewset(viewsets.ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSerilaizer

    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAuthenticatedOrReadOnly]

    #throttle_classes=[AnonRateThrottle,UserRateThrottle]
    throttle_classes=[AnonRateThrottle,JsckRateThrottle]


