
from functools import partial
from django.shortcuts import render
import io
from myapp.models import Student
from .serializers import StudentSerializers
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from myapp import serializers


@csrf_exempt
def student_api(request):
    if request.method=='GET':
        json_data=request.body
        stream=io.BytesIO(json_data)

        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializers(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type='application/json')
        stu=Student.objects.all()   
        serializer=StudentSerializers(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    if request.method == "POST":
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
        return HttpResponse(json_data,content_type="application/json")

        
    if request.method=='PUT':
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id = pythondata.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializers(stu,data=pythondata,partial=True)#It can update data partially
        #serializer=StudentSerializers(stu,data=pythondata)#you can not update data partially,all data has to be updated
        if serializer.is_valid():
            serializer.save()
            res={"msg":"data updated"} 
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

    if request.method=="DELETE":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()

        res={'msg':'data deleted...'}
        #json_data=JSONRenderer().render(res)
        #return HttpResponse(json_data,content_type='application/json')

        #without using that two line we can user this single line of code

        return JsonResponse(res,safe=False)



