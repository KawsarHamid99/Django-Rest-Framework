from django.shortcuts import render,HttpResponse
from serializerapp.models import Teacher
from .serializers import TeacherSrializer
# Create your views here.
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#python manage.py drf_create_token <user>
#python manage.py drf_create_token kawsar

#at first import obtain_auth_token then use it at urls.py file
#http POST http://127.0.0.1:8000/gettoken/ username="kawsar" password="kawsar"

class Details(viewsets.ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class=TeacherSrializer

    #authentication_classes=[TokenAuthentication]
    #permission_classes=[IsAuthenticated]


def home(request):
    return HttpResponse("Hello")