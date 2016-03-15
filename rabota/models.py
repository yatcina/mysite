#-*- coding:utf-8 -*-
from django.db import models


# Create your models here.

class cam(models.Model):
    name = models.CharField(max_length=20, verbose_name=u'Имя камеры')
    adress = models.CharField(max_length=50, verbose_name=u'Место нахождения')
    detektor1 = models.CharField(max_length=20,verbose_name=u'Имя входа в первую область')
    detektor2 = models.CharField(max_length=20, verbose_name=u'Имя выхода из первой области')
    detektor3 = models.CharField(max_length=20, verbose_name=u'Имя входа во вторую область')
    detektor4 = models.CharField(max_length=20, verbose_name=u'Имя выхода из втрой области')
    file_name = models.CharField(max_length=30, verbose_name=u'Имя лога из настроек камер')
    ip_adress = models.CharField(max_length=40, verbose_name=u'IP адресс камеры')
    def __unicode__(self):
        return '%s %s %s %s %s %s %s %s' % (self.name, self.adress, self.detektor1, self.detektor2, self.detektor3, self.detektor4, self.file_name, self.ip_adress)

class event(models.Model):
    camera = models.ForeignKey(cam)
    data_time = models.DateTimeField()
    events = models.CharField(max_length=20)
    def __unicode__(self):
        return '%s' % (self.events)
class otchet_po_day(models.Model):
    camera_ot = models.ForeignKey(cam)
    data = models.DateField()
    vhod = models.IntegerField()
    vihod = models.IntegerField()
    srednee = models.IntegerField()
class otchet_po_hears(models.Model):
    cam_ot = models.ForeignKey(cam)
    data_ot_day = models.DateField()
    time_ot = models.TimeField()
    vhod_ot = models.IntegerField()
    vihod_ot = models.IntegerField()
    srednee_ot = models.IntegerField()

class Seria_name(models.Model):
    name = models.CharField(max_length=50)
    def __unicode__(self):
        return '%s %s' % (self.name, self.name)
class serega(models.Model):
    seria_name = models.ForeignKey(Seria_name)
    name = models.CharField(max_length=50)
    seria = models.CharField(max_length=500)
    def __unicode__(self):
        return '%s %s' % (self.name, self.seria)

