#!usr/bin/python
#-*- coding:utf-8 -*-

import mysql.connector
from mysql.connector import Error
import datetime

class inicialize():
    def connect(self):
        """ Connect to MySQL database """
        try:
            self.conn = mysql.connector.connect(host='localhost',
                                           database='shitalka',
                                           user='root',
                                           password='123')
            if self.conn.is_connected():
                print(u'Успешно')

        except Error as e:
            return e

        finally:
            return self.conn.close()
        return self.conn
    def loadfile(self,vol=''):
        try:
            self.f = open(vol,'r')
        except IOError:
            self.error = u'Ощибка файла %s нет на диске' % vol
            return self.error
        self.ishod_file = []
        for self.n in self.f:
            self.ishod_file.append(self.n[:-1])
        self.f.close()
        return self.ishod_file
    def baza(self,result,vol1,vol2,vol3,vol4):
        self.itog_masiv = []
        self.vhod2 = 0
        for self.n in result:
            self.vhod2 = self.n.find(vol1)
            if self.vhod2 == -1:
                self.vhod2 = self.n.find(vol2)
                if self.vhod2 == -1:
                     self.vhod2 = self.n.find(vol3)
                     if self.vhod2 == -1:
                         self.vhod2 = self.n.find(vol4)
                         if self.vhod2 == -1:
                             continue
            self.now_time = datetime.datetime.now()
            self.god = self.now_time.year
            self.a = str(self.god)+' '+str(self.n[0:15])
            self.data_time = datetime.datetime.strptime(self.a, '%Y %b  %d %H:%M:%S')
            self.itog_masiv.append(self.data_time)
            self.itog_masiv.append(self.n[self.vhod2+6:])
        return self.itog_masiv

    def zapis_v_basu(self,ishod_arry, vol):
        self.total = event.objects.filter(camera_id = vol.id).count()
        if self.total>1:
            self.LastTernR = event.objects.filter(camera_id = vol.id)[self.total-1:self.total]
        else:
            self.LastTernR = event.objects.filter(camera_id = vol.id)[0:1]
        if not self.LastTernR:
            self.n=0
            while self.n<len(ishod_arry):
                self.q =event.objects.create(camera_id = vol.id, data_time = ishod_arry[self.n], events = ishod_arry[self.n+1])
                self.q.save()
                self.n+=2
        else:
            self.n = 0
            self.a = self.LastTernR.get().data_time.strftime('%Y %b  %d %H:%M:%S')
            self.b = ishod_arry[len(ishod_arry)-2]
            self.b = datetime.datetime.strftime(self.b, '%Y %b  %d %H:%M:%S')
            self.c = ishod_arry[0]
            self.c = datetime.datetime.strftime(self.c, '%Y %b  %d %H:%M:%S')
            if self.a <= self.b:
                while self.n<len(ishod_arry):
                    self.b = ishod_arry[self.n]
                    self.b = datetime.datetime.strftime(self.b,'%Y %b  %d %H:%M:%S')
                    if self.a == self.b:
                        ishod_arry = ishod_arry[self.n:]
                        ishod_arry = ishod_arry[2:]
                        self.t = 0
                        while self.t<len(ishod_arry):
                            self.q =event.objects.create(camera_id = vol.id, data_time = ishod_arry[self.t], events = ishod_arry[self.t+1])
                            self.q.save()
                            self.t+=2
                    self.n+=2
            if self.a < self.c:
                self.n = 0
                while self.n<len(ishod_arry):
                    self.b = ishod_arry[self.n]
                    self.b = datetime.datetime.strftime(self.b,'%Y %b  %d %H:%M:%S')
                    self.q =event.objects.create(camera_id = vol.id, data_time = ishod_arry[self.n], events = ishod_arry[self.n+1])
                    self.q.save()
                    self.n+=2
            else:
                return "asas"
        return self


def process_zapisi():
    basedir = "e:\\ftp\detektor\kassa"
    b = os.listdir(basedir)
    file_names = []
    for n in b:
        p = n.split('_')
        if p[1] == 'MD.log':
            continue
        file_names.append(p[0])
    if file_names == []:
        error = u'В папке нет файлов'
    else:
        error = u'Все заверщилось без ощибок'
        n=0
        c = inicialize()
        while n<len(file_names):
            l = cam.objects.get(file_name = file_names[n])
            url_file = 'e:\\ftp\detektor\kassa\%s_MD.syslog' % (l.file_name)
            result = c.loadfile(url_file)
            vhod_detektor2 = 'event'+ ' ' + l.detektor3
            vihod_detektor2 = 'event'+' ' + l.detektor4
            vhod_detektor1 = 'event'+' ' + l.detektor1
            vihod_detektor1 = 'event'+ ' ' + l.detektor2
            ishod_arry = c.baza(result,vhod_detektor2,vihod_detektor2,vhod_detektor1,vihod_detektor1)
            c.zapis_v_basu(ishod_arry,l)
            n+=1
    p=u'OK'
    return p



#if __name__ == '__main__':





