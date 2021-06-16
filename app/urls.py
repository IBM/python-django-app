from django.urls import path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import views

external_apis = [
                 path('health/', views.health, name='health'),
                ]

schema_view = get_schema_view(
    openapi.Info(
        title='Django API', 
        default_version='v1',
        description="Swagger UI for this Django app",
        terms_of_service="https://www.google.com/policies/terms/",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
    patterns = external_apis,
    )

urlpatterns = [
               path('', views.index, name='index'),
               path("docs/", schema_view.with_ui('swagger'), name='swagger-ui'),
               path('404', views.handler404, name='404'),
               path('500', views.handler500, name='500'),
               ] + external_apis