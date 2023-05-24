from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter
routers=DefaultRouter()
routers.register("singer",views.SingerViewset,basename="SingerViewset")
routers.register("song",views.SongViewset,basename="SongViewset")
#routers.register("Hyper_Linked_Model_Viewset",views.Hyper_Linked_Model_Viewset,basename="Hyper_Linked_Model_Viewset")
routers.register("Nasted_SingerViewset",views.Nasted_SingerViewset,basename="Nasted_SingerViewset")


urlpatterns=[
    path("",include(routers.urls)),
]
