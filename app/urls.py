from django.conf.urls import url

from . import views

urlpatterns = [
               url(r'^$', views.index, name='index'),
               url(r'^health', views.health, name='health'),
               url(r'^404', views.handler404, name='404'),
               url(r'^500', views.handler500, name='500'),
               ]
