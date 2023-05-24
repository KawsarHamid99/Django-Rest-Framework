from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from .auth import CustomAuthentication
routers=DefaultRouter()
routers.register("studentapi",views.StudentClass,basename="studentapi")

urlpatterns=[
    path("",include(routers.urls)),
    # path("gettoken/",obtain_auth_token)
    path("gettoken/",CustomAuthentication.as_view())
]