#!usr/bin/python
#-*- coding:utf-8 -*-
from django.contrib import admin
from sites.models import navimenu, UserProfile
from django.contrib.auth.models import User

admin.site.register(navimenu)
admin.site.register(UserProfile)
