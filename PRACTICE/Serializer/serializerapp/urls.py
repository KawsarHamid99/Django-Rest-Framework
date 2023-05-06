from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static 
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token
from serializerapp.auth import CustomAuthtoken
router=DefaultRouter()
router.register('studentapi',views.Detais,basename="student")

urlpatterns=[
    path("",include(router.urls)),
    #path("auth/",include("rest_framework.urls",namespace="authen")),
    #path('gettoken/',CustomAuthtoken.as_view())
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)