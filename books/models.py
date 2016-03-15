#!usr/bin/python
#-*- coding:utf-8 -*-
from django.db import models

class Publisher(models.Model):
    name = models.CharField(max_length=30, verbose_name=u"Имя")
    address = models.CharField(max_length=50, verbose_name=u"Адрес:")
    city = models.CharField(max_length=60)
    state_province = models.CharField(max_length=30)
    country = models.CharField(max_length=30)
    website = models.URLField()

    class Meta:
        ordering = ["-name"]

    def __unicode__(self):
        return self.name

class Author(models.Model):
    salutation = models.CharField(max_length=10)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(blank=True)
    heatshot = models.ImageField(upload_to = 'tmp/')
    def __unicode__(self):
        return '%s %s' % (self.first_name, self.last_name)

class Book(models.Model):
    title = models.CharField(max_length=100)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher)
    publication_date = models.DateField()
    def __unicode__(self):
        return self.title

