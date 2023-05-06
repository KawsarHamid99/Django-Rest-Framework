from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('studentapi',views.StudentViewset,basename="studentview")

urlpatterns=[ 
    #path("home/",views.home,name="home"),
    path("",include(router.urls))

]