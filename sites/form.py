#!usr/bin/python
#-*- coding:utf-8 -*-
from django import forms
from registration.forms import RegistrationForm

class ExRegistrationForm(RegistrationForm):
    first_name = forms.CharField(max_length=50, label=u'Фамилия')
    last_name = forms.CharField(max_length=50, label=u'Имя')
    surname = forms.CharField(max_length=100, label=u'Отчество')




