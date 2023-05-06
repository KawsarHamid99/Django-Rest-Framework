from django.urls import path,include
from . import views 

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
router=DefaultRouter()
router.register("teacherapi",views.Details,basename="teacher")

from .auth import CustomAuthtoken
urlpatterns=[
    path("",include(router.urls)),
    #path("gettoken/",obtain_auth_token),
    path("gettoken/",CustomAuthtoken.as_view())   
]