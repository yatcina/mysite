#-*- coding:utf-8 -*-
import xml.dom.minidom
import urllib2
class parser:
    def __init__(self,vol):
        self.vol = vol
        self.f = urllib2.urlopen('http://www.cbr.ru/scripts/XML_daily.asp?date_req=').read()
        self.par1 = xml.dom.minidom.parseString(self.f)
        self.data = self.par1.getElementsByTagName('Valute')
    def val(self):
        for n in self.data:
         #   if n.attributes["ID"].value == self.vol:
                self.a = n.getElementsByTagName('Value')[0].firstChild.data
                self.b = n.getElementsByTagName('Name')[0].firstChild.data
                print self.a, self.b, n.attributes["ID"].value




s = parser ("R01215")
s.val()
print s.a



























