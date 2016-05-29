from django.conf.urls import patterns, url
from itcastsubject import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
