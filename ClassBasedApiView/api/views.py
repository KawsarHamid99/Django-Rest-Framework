from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import StudentSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView


 # Class based view

class StudentAPI(APIView):
    def get(self,request,pk=None,format=None):
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"created successfully"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def put(self,request,pk,format=None):
        id=pk
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"updated successfully"})
        return Response({'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    def patch(self,request,pk,format=None):
        id=pk
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":" Partial updated successfully"})
        return Response({'msg':serializer.errors},status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk,format=None):
        id=pk
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response({"msg":"deleted successfully..."})
            



 # form based view

@api_view(['GET','POST',"PUT","DELETE"]) 
def student_api(request):
    if request.method == 'GET':
        id=request.data.get("id")
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)


    if request.method =="POST":
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"user created"})
        
        return Response(serializer.errors )
    if request.method == "PUT":
        id =request.data.get("id")
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"updated successfully..."})
        return Response(serializer.errors )
    if request.method=="DELETE":
        id=request.data.get("id")
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response({"msg":" object deleted successfully..."})
    



@api_view(['GET','POST',"PUT","PATCH","DELETE"]) 
def student_api_brawser(request,pk=None):
    if request.method == 'GET':
        id=pk
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)


    if request.method =="POST":
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"user created"},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


    if request.method == "PUT":
        id = pk
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"complete updated successfully..."})
        return Response(serializer.errors )

    if request.method == "PATCH":
        id = pk
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"Pirtially updated successfully..."})
        return Response(serializer.errors )


    if request.method=="DELETE":
        id= pk
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response({"msg":" object deleted successfully..."})
    