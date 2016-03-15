#!usr/bin/python
#-*- coding:utf-8 -*-
from django.conf.urls import *
from django.contrib.auth.views import login
from sites.models import navimenu


urlpatterns = patterns('polls.views',
    url(r'^hello/$','hello'),
    url(r'^meta/$','display'),
    url(r'^time/$','current_datetime'),
    url(r'^time/plus/(\d{1,2})/$','hours_ahread'),
    url(r'^$', login),
    )
