from django.urls import path
from . import views

urlpatterns= [ 
     # Class based view
    path("",views.StudentAPI.as_view()),
    path("<int:pk>/",views.StudentAPI.as_view()),

    # form based view
    path("bra/<int:pk>",views.student_api_brawser),
    path("bra/",views.student_api_brawser)
]