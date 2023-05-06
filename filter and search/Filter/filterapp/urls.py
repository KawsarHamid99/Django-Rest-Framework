from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
routers=DefaultRouter()
routers.register("studentview",views.StudentViewset,basename="studentview")

urlpatterns=[
    path("home/",views.home),
    path("",include(routers.urls))
] 