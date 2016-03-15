#!usr/bin/python
#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from registration.signals import user_registered


# Create your models here.

class navimenu(models.Model):
    name = models.CharField(max_length=40, verbose_name=u'имя')
    title = models.CharField(max_length=40)
    url = models.URLField(max_length=200)

    def __unicode__(self):
        return self.name

class UserProfile(models.Model):
    user = models.ForeignKey(User, unique = True)
    surname = models.CharField(max_length=100, verbose_name=u'Фамилия:')

    def __unicode__(self):
        return self.surname
def user_registered_callback(sender, user, request, **kwargs):
    profile = UserProfile(user = user)
    profile.surname = request.POST['surname']
    user.first_name = request.POST['first_name']
    user.last_name = request.POST['last_name']
    user.save()
    profile.save()
user_registered.connect(user_registered_callback)


