#!usr/bin/python
#-*- coding:utf-8 -*-
from django.conf.urls import *
from sites import views
from sites.form import ExRegistrationForm
from registration.backends.default.views import RegistrationView

urlpatterns = patterns('',
   url(r'^accounts/password/reset/$', 'django.contrib.auth.views.password_reset', {'post_reset_redirect' : '/accounts/password/reset/done/'},name="password_reset"),
   url(r'^accounts/password/reset/done/$','django.contrib.auth.views.password_reset_done'),
   url(r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm', {'post_reset_redirect' : '/accounts/password/done/'}),
   url(r'^accounts/password/done/$', 'django.contrib.auth.views.password_reset_complete'),
   url(r'^accounts/register/$', RegistrationView.as_view(form_class=ExRegistrationForm), name = 'registration_register' ),
   url(r'^accounts/', include('registration.backends.default.urls')),
   url(r'^sisadmin/logout/$',views.LogoutView.as_view()),
    )
