from django.shortcuts import render

from .models import Student
from .serilaizers import StudentSerializer

from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import BaseAuthentication,SessionAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

# Create your views here.
def home(request):
    return render(request,"home.html")


class StudentView(ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    authentication_classes=[JWTAuthentication]
    permission_classes=[IsAuthenticated]

