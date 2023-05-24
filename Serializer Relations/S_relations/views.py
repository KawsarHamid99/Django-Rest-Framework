from django.shortcuts import render,HttpResponse
from .models import Singer,Song

from .serializers import SingerSerializer,SongSerializer,Hyper_Linked_Model_Serializer,Nasted_Serializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.
def home(request):
    return HttpResponse("hello")

class SingerViewset(ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=SingerSerializer
    #serializer_class=Nasted_Serializer


class SongViewset(ModelViewSet):
    queryset=Song.objects.all()
    serializer_class=SongSerializer


class Hyper_Linked_Model_Viewset(ModelViewSet):
    queryset=Singer.objects.all()
    serializer_class=Hyper_Linked_Model_Serializer




class Nasted_SingerViewset(ModelViewSet):
    queryset=Singer.objects.all()

    serializer_class=Nasted_Serializer