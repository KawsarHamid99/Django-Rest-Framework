from django.shortcuts import render,HttpResponse
from django.http import JsonResponse

from .models import Student
from .serializer import StudentSerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.
def student_details(request):
    stu = Student.objects.get(id=2)
    serializer=StudentSerializer(stu)
    json_data=JSONRenderer().render(serializer.data)
    print("---------------------------------------")
    print(stu)
    print("---------------------------------------")
    print(serializer)
    print("---------------------------------------")
    print(json_data)
    print("---------------------------------------")
    return HttpResponse(json_data,content_type='application/json')

def student_details_by_pk(request,pk):
    stu = Student.objects.get(id=pk)
    serializer=StudentSerializer(stu)
    json_data=JSONRenderer().render(serializer.data)
    print("---------------------------------------")
    print(stu)
    print("---------------------------------------")
    print(serializer)
    print("---------------------------------------")
    print(json_data)
    print("---------------------------------------")
    return HttpResponse(json_data,content_type='application/json')

def student_list(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    #json_data=JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)


