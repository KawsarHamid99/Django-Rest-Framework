from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import StudentSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

#use this command on the cmd
# 1
# python manage.py drf_create_token <username>
#EX: python manage.py drf_create_token kawsar

#2 user reqest for token
# http POST http://127.0.0.1:8000/<pagename>/ username="<user>" password="pass"
# http POST http://127.0.0.1:8000/gettoken/ username="kawsar" password="kawsar"




#GET request:
#http http://127.0.0.1:8000/studentapi/

#Get Request with auth 
#http http://127.0.0.1:8000/studentapi/'Authorization:Token 53f37471f322f1ba98016eb54c89a888a14cb64a'

# POST Request/Submitting Form
#http -f POST http://127.0.0.1:8000/studentapi/ name=kawsae roll=200 city=khulna 'Authorization:Token 53f37471f322f1ba98016eb54c89a888a14cb64a'

# PUT Request
#http PUT http://127.0.0.1:8000/studentapi/4/ name=kawsae roll=200 city=khulna 'Authorization:Token 53f37471f322f1ba98016eb54c89a888a14cb64a'

# DELETE Request
#http DELETE http://127.0.0.1:8000/studentapi/4/'Authorization:Token 53f37471f322f1ba98016eb54c89a888a14cb64a'

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

