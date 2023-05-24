from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
routers=DefaultRouter()
routers.register("studentapi",views.StudentView,basename="studentview")
urlpatterns=[ 
    path("home/",views.home,name="home"),
    path("",include(routers.urls)),
    path("auth/",include('rest_framework.urls',namespace="rest_framework")),

    path("gettoken/",TokenObtainPairView.as_view(),name="gettoken"),
    path("refreshtoken/",TokenRefreshView.as_view(),name='refreshtoken'),
    path('verifytoken/',TokenVerifyView.as_view(),name="verifytoken"),


]