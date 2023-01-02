from django.urls import path
from . import views

urlpatterns= [ 
    path("",views.student_api),
    path("bra/<int:pk>",views.student_api_brawser),
    path("bra/",views.student_api_brawser)
]