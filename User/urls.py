from django.conf.urls import patterns, url
from User import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^base$', views.base, name='base'),
    url(r'^codes', views.codes, name='codes'),
    url(r'^about', views.about, name='about'),
    url(r'^contact', views.contact, name='contact'),
    url(r'^gallery', views.gallery, name='gallery'),
    url(r'^baidumap', views.baidumap, name='baidumap'),
)
