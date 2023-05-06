from django.shortcuts import render
from rest_framework import viewsets
from .models import Student
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
# Create your views here.

#this is for global pagination 
class Page_Number_Pagination(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer



from .mypaginations import MyPageNumberPagination
class perViewPagination(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class=MyPageNumberPagination


from .mypaginations import MyLimitOffsetPagination
class Limit_Offset_pagination(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class=MyLimitOffsetPagination


from .mypaginations import MyCursorPagination
class Cursor_pagination(ListAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    pagination_class=MyCursorPagination

