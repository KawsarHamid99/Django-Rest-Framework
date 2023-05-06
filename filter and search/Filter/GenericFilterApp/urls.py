from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter
routers=DefaultRouter()
routers.register("genericfilter",views.GenericFilter,basename="genericfilter")

urlpatterns=[
    path("",include(routers.urls)),
    #path("auth",include("rest_framework.urls",namespace="rest_framework")),
    path("list/",views.GenericLIST.as_view()),
]
