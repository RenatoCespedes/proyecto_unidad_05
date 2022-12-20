from rest_framework import (routers)
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView
)
from django.urls import (path,include)
from payments.v2 import  api

urlpatterns=[]
router = routers.DefaultRouter()
router.register(r'pay',api.ApiPayment,'pay')
router.register(r'service',api.ApiService,'servicios')
router.register(r'expired',api.ApiExpired,'expired')

urlpatterns += router.urls