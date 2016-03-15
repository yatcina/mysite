#-*- coding:utf-8 -*-
from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
import datetime

def hello(request):
    hel = u"Здравствуй, МИР!"
    return render_to_response('hello.html',{'hello':hel})
def current_datetime(request):
    now = datetime.datetime.now()
    return render_to_response('current_datetime.html',{'current_date': now})
def hours_ahread(request, offset):
    try:
      offset = int(offset)
    except ValueError:
      raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    return render_to_response('hours_ahead.html',{'hour_offset':offset,'next_time':dt})
def display(request):
    values = request.META['REMOTE_ADDR']
    return HttpResponse('Ваш %s' % values)
