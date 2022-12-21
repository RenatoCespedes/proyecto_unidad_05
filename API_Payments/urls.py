"""API_Payments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include,re_path
from drf_yasg import (openapi)
from drf_yasg.views import (get_schema_view)
from rest_framework.permissions import (AllowAny)
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView
)

schema_view = get_schema_view(
    openapi.Info(
        title="Pagos v2 API",
        default_version="v2",
        description="Proyecto Pagos V2",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@contact.com"),
        license=openapi.License(name="RE License")
    ),
    public=True,
    permission_classes=[AllowAny],
    urlconf="payments.v2.urls"
    
)

schema_view_user = get_schema_view(
    openapi.Info(
        title="User API",
        default_version="v2",
        description="User API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@contact.com"),
        license=openapi.License(name="RE License")
    ),
    public=True,
    permission_classes=[AllowAny],
    urlconf="users.urls"
    
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('payments.urls'),name='pagos'),
    path('api/v1/users/', include('users.urls'),name='usuariosv1'),
    path('api/v2/users/', include('users.urls'),name='usuariosv2'),
    path('api/v2/', include('payments.v2.urls')),
    re_path(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    re_path(r'^swagger/pagos$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^swagger/user$', schema_view_user.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),

]



