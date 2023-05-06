from django.shortcuts import render,HttpResponse
from .models import Student 
from .serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView


from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly
from rest_framework.permissions import DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
# Create your views here.
from .custompermissions import MyPermission 

#Permission: AllowAny,IsAuthenticated,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermission,
# DjangoModelPermissionOrAnonReadOnly,DjangoObjectPermission,CustomPermission


class StudentLC(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[SessionAuthentication]
    #permission_classes=[DjangoModelPermissionsOrAnonReadOnly]
    permission_classes=[MyPermission]



class StudentRU(RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    


class StudentRD(RetrieveDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentRUD(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    authentication_classes=[SessionAuthentication]
    permission_classes=[DjangoModelPermissionsOrAnonReadOnly]


    

