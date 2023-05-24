from django.urls import path
from . import views



urlpatterns=[
    path("",views.StudentLC.as_view()),
    path("<int:pk>",views.StudentRUD.as_view()),
    path("ru/<int:pk>",views.StudentRU.as_view()),
    path("rd/<int:pk>",views.StudentRD.as_view()),

]


##it is an example
# from rest_framework.routers import DefaultRouter
# router=DefaultRouter()
# router.register('studentapi',views.StudentViewset,basename="studentview")

# urlpatterns=[ 
#     #path("home/",views.home,name="home"),
#     path("",include(router.urls)),
#     path("auth/",include('rest_framework.urls',namespace="rest_framework")),
    

# ]