from django.urls import path
from . import  views
urlpatterns = [ 
    path("",views.student_details,name="student_details"),
    path("<int:pk>/",views.student_details_by_pk,name="student_details_pk"),
    path("list/",views.student_list,name="student_list"),
]