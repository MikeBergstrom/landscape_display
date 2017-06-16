from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<num>\d+)$', views.results),
    url(r'^fail$', views.fail)
]