from django.urls import path,include
from . import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('teacherapi',views.StudentModelViewset,basename="teacherview")

urlpatterns=[
    path("",include(router.urls)),
    path('auth',include('rest_framework.urls',namespace="rest_framework"))

]