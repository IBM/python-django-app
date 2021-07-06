from django.urls import path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
from . import views


urlpatterns = [
               path('', views.index, name='index'),
               path('health/', views.health, name='health'),
               path('schema/', SpectacularAPIView.as_view(), name='schema'),
               path('docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
               path('404', views.handler404, name='404'),
               path('500', views.handler500, name='500'),
               ]