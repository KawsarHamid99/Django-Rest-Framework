from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser


# permission classes
# 1. AllowAny
# 2. IsAuthenticated
# 3. IsAdminUser
# 4. IsAuthenticatedOrReadOnly
# 5. DjangoModelPermissions
# 6. DjangoModelPermissionsOrAnonReadOnly
# 7. DjangoObjectPermissions
# 8. CustomPermissions

class StudentLC(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]


    #permission_classes=[AllowAny] #without othentication it will work
    #permission_classes=[IsAdminUser] # if  user is is Stuff


class Student_RU(RetrieveUpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAdminUser]


class Student_RD(RetrieveDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class Student_RUD(RetrieveUpdateDestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer