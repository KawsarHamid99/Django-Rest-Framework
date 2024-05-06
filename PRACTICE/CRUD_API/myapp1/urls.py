from django.urls import path
from . import views
urlpatterns=[
    path("home",views.home),
    path("",views.student_api,name="student_api")
]