#!usr/bin/python
#-*- coding:utf-8 -*-
from django.conf.urls import *
from django.contrib import admin
from django.conf import settings
from filebrowser.sites import site
from django.contrib.auth.views import login, logout

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/filebrowser/', include(site.urls)),
    url(r'^pages/', include('django.contrib.flatpages.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/login/$',  login),
    url(r'^accounts/logout/$', logout),


)

urlpatterns += patterns('',
  url(r'',include('polls.urls')),
  url(r'',include('rabota.urls')),
  url(r'',include('books.urls')),
  url(r'',include('sites.urls')),
  )

if settings.DEBUG:
    urlpatterns += patterns('',
    (r'^tmp/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT}),
    (r'^/tmp/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.MEDIA_ROOT}),
    (r'^statics/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
    (r'^/statics/(?P<path>.*)$', 'django.views.static.serve',
         {'document_root': settings.STATIC_ROOT}),
    )
