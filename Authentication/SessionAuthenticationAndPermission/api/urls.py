from django.urls import path
from . import views



urlpatterns=[
    path("",views.StudentLC.as_view()),
    path("<int:pk>",views.StudentRUD.as_view()),
    path("ru/<int:pk>",views.StudentRU.as_view()),
    path("rd/<int:pk>",views.StudentRD.as_view()),

]