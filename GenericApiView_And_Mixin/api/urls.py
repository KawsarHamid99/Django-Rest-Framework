from django.urls import path
from . import views

urlpatterns= [ 
     # Class based view
    path("",views.StudentList.as_view()),
    path("create",views.StudentCreate.as_view()),
    path("<int:pk>/",views.StudentRetrieve.as_view()),
    path("update/<int:pk>/",views.Studentupdate.as_view()), 
    path("delete/<int:pk>/",views.StudentDestroy.as_view()),
    ########################################################
    path("crud/",views.Student_LC.as_view(),name="read-all-and-create"), 
    path("crud/<int:pk>",views.Student_RUD.as_view()), 

      
]