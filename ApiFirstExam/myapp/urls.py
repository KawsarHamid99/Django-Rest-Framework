from django.urls import path
from . import views
urlpatterns=[ 
    path("p",views.show,name="showdata"),
    path("",views.StudentApi.as_view(),name="showdata")
]

