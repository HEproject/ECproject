from django.conf.urls import patterns, url
from User import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^base$', views.base, name='base'),
    url(r'^base2$', views.base2, name='base2'),
    url(r'^one', views.one, name='one'),
)
