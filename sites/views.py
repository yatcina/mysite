#-*- coding:utf-8 -*-
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from sites.models import navimenu
from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout


def index(request):
    menu = navimenu.objects.all()
    if request.user.is_authenticated():
        a = request.user.username
        autuser = u'Вы авторизированы',a
    else:
        autuser = None
    return render_to_response('index.html',{'menu':menu, 'autuser':autuser})

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect('/')









