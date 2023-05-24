from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

router=DefaultRouter()
router.register('studentapi',views.StudentViewset,basename="studentview")

urlpatterns=[ 
    #path("home/",views.home,name="home"),
    path("",include(router.urls)),
    #path("auth/",include('rest_framework.urls',namespace="rest_framework")),
    path("gettoken/",TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('refreshtoken/',TokenRefreshView.as_view(),name="koken_refresh"),
    path('verifytoken/',TokenVerifyView.as_view(),name="token_verify"),
]