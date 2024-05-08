from django.shortcuts import render,HttpResponse
from .models import Students
from .serializers import StudentSerializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets

# Create your views here.
def home(request):
    return HttpResponse("hello world")

class MyViewClass(viewsets.ModelViewSet):
    queryset=Students.objects.all()
    serializer_class=StudentSerializers
    



