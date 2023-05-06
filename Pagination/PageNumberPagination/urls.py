from django.urls import path,include

from rest_framework.routers import DefaultRouter

from . import views

from rest_framework.routers import DefaultRouter
routers=DefaultRouter()
routers.register('student',views.Page_Number_Pagination,basename="studentpagination")

per_route=DefaultRouter()
per_route.register('perviewpagination',views.perViewPagination,basename="perviewpagination")

urlpatterns=[
    path("",include(routers.urls)),
    path("perview/",include(per_route.urls)),
    path("limit_shaffle/",views.Limit_Offset_pagination.as_view()),
    path("cursor/",views.Cursor_pagination.as_view()),
]