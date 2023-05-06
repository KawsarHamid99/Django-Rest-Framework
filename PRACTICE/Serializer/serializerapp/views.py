from .models import Teacher
from .serializer import Studentserializer
from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.views import APIView

from rest_framework.authentication import SessionAuthentication,TokenAuthentication,BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from .custompermission import Custom
# permission classes
# 1. AllowAny
# 2. IsAuthenticated
# 3. IsAdminUser
# 4. IsAuthenticatedOrReadOnly
# 5. DjangoModelPermissions
# 6. DjangoModelPermissionsOrAnonReadOnly
# 7. DjangoObjectPermissions
# 8. CustomPermissions

class Detais(viewsets.ModelViewSet):
    queryset=Teacher.objects.all()
    serializer_class=Studentserializer

    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAuthenticated]




    



