from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from django.urls import path, include
from django.contrib import admin


schema_view = get_schema_view(
    openapi.Info(
        title="SMS MANAGER BACKEND APIs",
        default_version='v1',
        description="APIs made to be integrated with Jambopay SMS portal and extend API sintegrations service to clients",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="larry.katuva@gmail.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('src.urls.authentication_urls')),
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
         cache_timeout=0), name='schema-redoc')
]
