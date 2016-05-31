from django.conf.urls import patterns, url
from goodslib import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    
)
