from django.urls import path
from . import views

urlpatterns= [ 

    path("",views.StudentList.as_view()),
    path("create",views.StudentCreate.as_view()),
    path("retrieve/<int:pk>",views.StudentRetrieve.as_view()),
    path("update/<int:pk>",views.StudentUpdate.as_view()),
    path("destroy/<int:pk>",views.StudentDestroy.as_view()),
    ###################### Combine Class #######################
    path("LC",views.StudentLC.as_view()),
    path("RU/<int:pk>",views.Student_RU.as_view()),
    path("RD/<int:pk>",views.Student_RD.as_view()),
    path("RUD/<int:pk>",views.Student_RUD.as_view()),


      
]