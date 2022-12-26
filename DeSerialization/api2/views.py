from django.shortcuts import render,HttpResponse
import io
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer

from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def student_create(request):
    if request.method=='POST':
        print(f"request------{request}")
        json_data=request.body
        print(f"json data------{json_data}")
        stream=io.BytesIO(json_data)
        print(stream)
        pythondata=JSONParser().parse(stream)
        print(pythondata)
        serializer= StudentSerializer(data=pythondata)
        print(serializer)

        if serializer.is_valid():
            serializer.save()
            res={'msg':'data created'}
            json_data=JSONRenderer().render(res)
            print(f"json data===={json_data}")
            return HttpResponse(json_data,content_type='applicaton')

        json_data=JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='applicaton')


