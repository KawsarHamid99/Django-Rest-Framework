from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import Student
from .serializer import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.http import JsonResponse
# Create your views here.

@method_decorator(csrf_exempt,name='dispatch')
class StudentApi(View):
    def get(self,request,*args,**kwargs):
        data=request.body
        stream=io.BytesIO(data)
        pythondata=JSONParser().parse(stream)
        id= .get('id',None)

        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type="application/json_data")
        else:
            stu=Student.objects.all()
            serializer=StudentSerializer(stu,many=True)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type="application/json_data")

    def post(self,request,*args,**kwargs):
        data=request.body
        stream=io.BytesIO(data)
        pythondata=JSONParser().parse(stream)
        serializer=StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            res={"msg":"created successfully"}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type="application/json_data")
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/json_data")


    def put(self,request,*args,**kwargs):
        data=request.body
        stream=io.BytesIO(data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        stu=Student.objects.get(id=id)

        serializer=StudentSerializer(stu,data=pythondata,partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'updated...'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type="application/json_data")
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/json_data")

    def delete(self,request,*args,**kwargs):
        data=request.body
        stream=io.BytesIO(data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        stu=Student.objects.get(id=id)
        stu.delete()
        res={"msg":'object has been deleted'}
        return JsonResponse(res)




@csrf_exempt
def show(request):
    if request.method=="GET":
        data=request.body
        stream=io.BytesIO(data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)

        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type="application/json_data")
        else:
            stu=Student.objects.all()
            serializer=StudentSerializer(stu,many=True)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data,content_type="application/json_data")
    if request.method=="POST":
        data=request.body
        print(f"data------->>>>{data}")
        print(f"data type------->>>>{type(data)}")
        stream=io.BytesIO(data)
        print(f"stream------->>>>{stream}")
        pythondata=JSONParser().parse(stream)
        print(f"pythondata------->>>>{pythondata}")
        serializer=StudentSerializer(data=pythondata)
        print(f"serializer------->>>>{serializer}")
        if serializer.is_valid():
            serializer.save()
            res={"msg":"created successfully"}
            json_data=JSONRenderer().render(res)
            print(f"json_data------->>>>{json_data}")
            return HttpResponse(json_data,content_type="application/json_data")
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/json_data")
    
    if request.method=="PUT":
        data=request.body
        stream=io.BytesIO(data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        stu=Student.objects.get(id=id)

        serializer=StudentSerializer(stu,data=pythondata,partial=True)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            res={'msg':'updated...'}
            json_data=JSONRenderer().render(res)
            return HttpResponse(json_data,content_type="application/json_data")
        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type="application/json_data")

    if request.method=="DELETE":
        data=request.body
        stream=io.BytesIO(data)
        pythondata=JSONParser().parse(stream)
        id=pythondata.get('id',None)
        stu=Student.objects.get(id=id)
        stu.delete()
        res={"msg":'object has been deleted'}
        return JsonResponse(res)


    return HttpResponse("Hello world")
