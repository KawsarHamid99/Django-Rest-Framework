from django.urls import path
from . import views

urlpatterns= [ 

   
    ###################### Combine Class #######################
    path("",views.StudentLC.as_view()),
    path("RU/<int:pk>",views.Student_RU.as_view()),
    path("RD/<int:pk>",views.Student_RD.as_view()),
    path("RUD/<int:pk>",views.Student_RUD.as_view()),


      
]