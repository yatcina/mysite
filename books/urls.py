#!usr/bin/python
#-*- coding:utf-8 -*-
from django.conf.urls import *
from books import views


urlpatterns = patterns('',

   url(r'^search-form/$',views.search_form),
    url(r'^search/$',views.search),
    url (r'^contact/$',views.contact),
    url (r'^contact/thanks/$',views.thanks),
    url (r'^viewbook/$',views.view_books),

    )