from functools import partial
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render

from .models import Student
from .serializers import StudentSerializers
from django.views.decorators.csrf import csrf_exempt 
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer

import io
@csrf_exempt
def student_api(request):
    if request.method=="GET":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)

        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializers(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type="application/json")

        stu=Student.objects.all()
        serializer=StudentSerializers(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type="application/json")
    if request.method=="POST":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializers(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data created'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type="application/json")
        json_data=JSONRenderer().render(serializer.error)
        return HttpResponse(json_data,content_type="application/json")
    if request.method=="PUT":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializers(stu,data=pythondata,partial=True)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'data updated'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type="application/json")
        json_data=JSONRenderer().render(serializer.error)
        return HttpResponse(json_data,content_type="application/json")
    
    if request.method=="DELETE":
        json_data=request.body
        stream=io.BytesIO(json_data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        res={'msg':'data deleted'}

        return JsonResponse(res,safe=False)









