from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("",views.StudentViewset,basename="stuApi")
urlpatterns=[
    path("",include(router.urls)),
    #path("",views.StudentViewset.as_view())
]