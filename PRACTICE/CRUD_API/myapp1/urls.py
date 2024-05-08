from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

routers=DefaultRouter()
routers.register("api",views.MyViewClass,basename="api")


urlpatterns=[
    path("home",views.home),
    path("",include(routers.urls)),
    path("auth/",include('rest_framework.urls',namespace='rest_framework'))

]