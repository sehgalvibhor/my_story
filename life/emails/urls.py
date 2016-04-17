from django.conf.urls import patterns, url
from emails import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^thanks/$',views.thanks,name='thanks'),)