from django.urls import path,include
from . import views
from django.contrib import admin
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

#create user request token
from rest_framework.authtoken.views import obtain_auth_token
from .authtoken import CustomAuthToken


router.register("stuapi",views.StudentModelViewSet,basename="studentApi")
urlpatterns= [ 
    path("",include(router.urls)),
    path("gettoken/",obtain_auth_token),
    
    
    #custom token
    path("posttoken/",CustomAuthToken.as_view()),
    
]