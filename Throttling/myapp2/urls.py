from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
routers=DefaultRouter()
routers.register("teacher",views.Teacherviewset,basename="teacher")

urlpatterns=[
    path("",include(routers.urls)),

    path("rud/<int:pk>/",views.teacherRUD.as_view()),
    path("list/",views.teacherList.as_view()),
]