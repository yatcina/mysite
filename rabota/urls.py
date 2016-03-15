#!usr/bin/python
#-*- coding:utf-8 -*-
from django.conf.urls import *
from rabota import views


urlpatterns = patterns('',

   url(r'^rabota/$',views.rabota),
   url(r'^chitalka/$',views.shitalka),
   url(r'^settings/([0-9]{2})/([0-9]+)/$',views.settings_camera),
   url(r'^proces-sapisi/$',views.process_zapisi),
   url(r'^zapis/$',views.zapis),
   url(r'^risovalka/$',views.risovalka),
   url(r'^isoval/$',views.isoval),
   url(r'^raschet/$',views.raschet),
   url(r'^raschet/([^/]+)/$',views.raschet1),
   url(r'^settings_raschet/([^/]+)/$',views.settings_raschet),
    )