#!usr/bin/python
#-*- coding:utf-8 -*-
from django import template
from sites.models import navimenu
from rabota.models import cam,otchet_po_day,otchet_po_hears,event

register = template.Library()

@register.filter(name='color_text')
def color_text(value):
    arg = []
    for i in value:
        if i.isupper():
            arg.append('<b style="color:red">'+i+'</b>')
        else:
            arg.append(i)
    return arg

@register.filter(name='color_text_a')
def color_text_a(value):
    arg = []
    for i in value:
        if i == 111111:
            arg.append('<b style="color:black">'+'-------------------------------'+'</b>')
        elif type(i) == str:
            arg.append('<b style="color:red">'+i+'</b>')
        else:
            arg.append(i)
    return arg

@register.inclusion_tag('menu.html')
def menu():
    l = navimenu.objects.all()
    return {'menu':l}

@register.filter(name = 'basa')
def basa_ot(vol):
    a = vol.date()
    result = otchet_po_hears.objects.filter(data_ot_day = a)
    return result