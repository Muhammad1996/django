from django.conf.urls import url
from rango import views
from rango import about

urlpatterns = [
    url(r'^about/', views)
    url(r'^$', views.index, name='index'),
    ]
