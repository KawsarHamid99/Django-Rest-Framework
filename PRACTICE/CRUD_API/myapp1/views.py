from django.shortcuts import render,HttpResponse
from .models import Students
from .serializers import StudentSerializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework import serializers
# Create your views here.
def home(request):
    return HttpResponse("hello world")

@csrf_exempt
def student_api(request):
    if request.method=="GET":
        print("GET ---->>  student_api")
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)

        if id is not None:
            stu=Students.objects.get(id=id)
            serializer=StudentSerializers(stu)
            jsondata=JSONRenderer().render(serializer.data)
            return HttpResponse(jsondata,content_type='application/json')
        
        stu=Students.objects.all()
        serializer=StudentSerializers(stu,many=True)
        print(serializer.data)
        jsondata=JSONRenderer().render(serializer.data)
        print(jsondata)
        return HttpResponse(jsondata,content_type='applicaton/json')
    
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializers(data=pythondata)
        
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializers.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=="PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        stu=Students.objects.get(id=id)
        serializer=StudentSerializers(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={"msg":"updated"}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializers.errors)
        return HttpResponse(json_data,content_type='application/json')
    
    if request.method=="DELETE":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)

        id=pythondata.get('id',None)
        stu=Students.objects.get(id=id)
        stu.delete()
        res={'msg':'deleted successfully'}

        json_data=JSONRenderer().render(res)
        return HttpResponse(json_data,content_type='application/json')
    




