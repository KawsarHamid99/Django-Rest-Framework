from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin,CreateModelMixin,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin


class StudentList(GenericAPIView,ListModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request,*arg,**kwarg):
        return self.list(request,*arg,**kwarg)


class StudentCreate(GenericAPIView,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def post(self,request,*arg,**kwarg):
        return self.create(request,*arg,**kwarg)


class StudentRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request,*arg,**kwarg):
        return self.retrieve(request,*arg,**kwarg)


class Studentupdate(GenericAPIView,UpdateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def put(self,request,*arg,**kwarg):
        return self.update(request,*arg,**kwarg)


class StudentDestroy(GenericAPIView,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def delete(self,request,*arg,**kwarg):
        return self.destroy(request,*arg,**kwarg)



# All in a single class
class Student_LC(GenericAPIView,ListModelMixin,CreateModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

    def get(self,request,*arg,**kwarg):
        return self.list(request,*arg,**kwarg)

    def post(self,request,*arg,**kwarg):
        return self.create(request,*arg,**kwarg)

class Student_RUD(GenericAPIView,RetrieveModelMixin,UpdateModelMixin,DestroyModelMixin):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer


    def get(self,request,*arg,**kwarg):
        return self.retrieve(request,*arg,**kwarg)
    
    def put(self,request,*arg,**kwarg):
        return self.update(request,*arg,**kwarg)
    
    def delete(self,request,*arg,**kwarg):
        return self.destroy(request,*arg,**kwarg)

