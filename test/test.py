#!usr/bin/python
#-*- coding:utf-8 -*-
import sys, io
from string import maketrans
import re

try:
    f = open('test123.txt','r')
except IOError:
    print ("Нет файла")
ishod = f.read()
f.close()

#ishod = '''Help text of model form odelds for ManyToManyField fields HTML rendering of model form fields correspondmod el ManyToManyField model Hmode lext of model fields used to get the hard-coded sentence: Hold down "Control", or "Command" on a Mac, to select more than one.
#(or its translation to the active locale) imposed as the help legend shown along them if neither model nor form help_text attributes were specified by the user (or this string was appended to any help_text that was provided).
# Since this happened at the model layer, there was no way to prevent the text from appearing in cases where it was not applicable such as form fields that implement user interactions that do not involve a keyboard and/or a mouse.
#Starting with Django 1.6, as an ad-hoc temporary Help text of model backward-compatibility provision, tmo delic to add the "Hold down..." sentence has been moved to the model form field layer and modified to add the text only when the associated widget is SelectMultiple or selected subclasses.
#The change can affect you in a backward incompatible way if you employ custom model form odelds and/or widgets for ManyToManyField model fields whose UIs do rely on the automatic provision of the mentioned hard-coded sentence. These form field implementations need to adapt to the new scenario by providing their own handling of the help_text attribute.
#Applications that use Django model form facilities together with Django built-in form fields and widgets are not affected but need to be aware of what’s described in Munging of help text of model form fields for ManyToManyField fields below.'''

#shablon = 'My father and brother opposed me because'
shablon = 'mod'

ishod = ishod.lower()
shablon = shablon.lower()
ishod_a = ishod.split(' ')
shablon_a = shablon.split(' ')

class dictori:
# Инициализация словаря
    def __init__(self):
        self.a = []
        self.a.append(dict.fromkeys(['a','j','s'],1))
        self.a.append(dict.fromkeys(['b','k','t'],2))
        self.a.append(dict.fromkeys(['c','l','u'],3))
        self.a.append(dict.fromkeys(['d','m','v'],4))
        self.a.append(dict.fromkeys(['e','n','w'],5))
        self.a.append(dict.fromkeys(['f','o','x'],6))
        self.a.append(dict.fromkeys(['g','p','y'],7))
        self.a.append(dict.fromkeys(['h','q','z'],8))
        self.a.append(dict.fromkeys(['i','r'],9))
        self.a.append(dict.fromkeys(['.','/',':',';','"','`','-','_'],0))
        self.b = []
        self.b.append(dict([('a',1),('b',2),('c',3),('d',4),('e',5),('f',6),('g',7),('h',8),('i',9),('j',10),('k',11),('l',12),('m',13),('n',14),('o',15),('p',16),('q',17),('r',18),('s',19),('t',20),('u',21),('v',22),('w',23),('x',24),('y',25),('z',26),('/',0),('.',0),('/',0),(':',0),('"',0),('`',0),('-',0),('=',0),('_',0)]))
#Функция перефода букв в пифагор и обычную (пифагор vol2=1, j, обычный vol2 любой)
    def pifagor1(self, vol1, vol2):
        if vol2 == 1:
            self.zn = self.a
        else:
            self.zn = self.b
        n=0
        while n<len(self.zn):
            if self.zn[n].get(vol1):
                return self.zn[n].get(vol1)
            n+=1
        return self.a[9].get('-')
#Функция преоброзования списка по словам
def format(vol1, vol2):
    m = 0
    n = 0
    u =[]
    y=[]
    while n<len(vol1):
        while m<len(vol2):
            u.append(vol1[n+m])
            m+=1
            if n+m == len(vol1):
                break
        m=0
        strok = ' '.join(u)
        y.append(strok)
        u=[]
        n+=1
    w=''
    e=[]
    for n in y:
        r = n.split(' ')
        for q in r:
           w = w+q
        e.append(w)
        w=''
    return e

# Функция сумирования чисел букв и возрощает список  = сумме числел букв в слове
def progonka(f,znach,v):
    a=0
    result = []
    result1 = 0
    result2 = []
    result3 = []
    for n in f:
       while a<len(n):
           result.append(v.pifagor1(n[a],znach))
           result1 = result1+int(v.pifagor1(n[a],znach))
           a+=1
       a=0
       result2.append(result1)
       result1 = 0
    return result2
# Поиск значений по шаблону vol = 1 полный поиск по шаблону, любое число поиск по словам. vol1 - исходный список vol2 - шаблон
def poln_pifag(vol,vol1,vol2):
    q=[]
    p = 0
    i=0
    for n in vol1:
        for m in vol2:
            if vol == 1:
                if n == m and n == vol2[i]:
                    q.append(dict([(n,p)]))
                    i+=1
                if i==len(vol2):
                    i=0
            else:
                if m == n:
                    q.append(dict([(n,p)]))
        p+=1
    return q
# функция форщает исходный масив с найдеными фрагментами необходми значения из функции poln_pifag
def vozrat(vol):
    for n in vol:
        for key,ind in n.items():
            v = ishod_a[ind].upper()
            ishod_a[ind] = v
    konec = ' '.join(ishod_a)
    return konec
# Функция возрашает сумму всех чисел в предложении
def sun_pol(vol):
    rw=0
    wr=[]
    for n in vol:
        rw = rw+int(n)
    wr.append(rw)
    return wr
# Функция возрашает строку исходника.
def vozrat_pol(vol,vol1,vol2):
    for n in vol:
            for key,ind in n.items():
                t=0
                while t<len(vol1):
                    v = vol2[ind+t].upper()
                    vol2[ind+t] = v
                    t+=1
    konec = ' '.join(vol2)
    return konec


#print a
#print b
#print vozrat(poln_pifag(1,a,b))


def obrab(vol):
    vq=[]
    qv = []
    for n in vol:
        resul = n.split("\n")
        vq.append(resul)
    for ve in vq:
        for n in ve:
            if n =='':
                continue
            else:
                qv.append(n)
    return qv


ishod_a = obrab(ishod_a)
shablon_a = obrab(shablon_a)
v=dictori()
#a = progonka(ishod_a,1,v)
b = progonka(shablon_a,1,v)
r = progonka(shablon_a,2,v)

qw = format(ishod_a,shablon_a)
c = progonka(qw,1,v)
d = progonka(qw,2,v)
wr = sun_pol(b)
wb = sun_pol(r)
we = poln_pifag(1,c,wr)
wq = poln_pifag(1,d,wb)

def polrealpifag(vol,vol1,vol2,vol3):
    re = []
    for n in vol:
        for r,t in n.items():
            for m in vol1:
                for rm,tm in m.items():
                    if rm == vol2[0] and tm == t and r == vol3[0]:
                        re.append(dict([(r,t)]))
    return re

#print vozrat_pol(polrealpifag(we,wq,wb,wr),shablon_a,ishod_a)


ishod_q = ishod.split('.')
def chisla(vol,vol2):
    iss = []
    for m in vol:
        m=m+'.'
        iss.append(m)
    nn=0
    vv = []
    cc = []
    while nn<len(vol):
        vv = iss[nn]+str(sun_pol(progonka(iss[nn],1,vol2)))+str(sun_pol(progonka(iss[nn],2,vol2)))
        cc.append(vv)
        nn+=1
    return cc

#print chisla(ishod_q,v)

shablon_b = obrab(shablon_a)
ishod_b = obrab(ishod.split(' '))
pifagChisla = sun_pol(progonka(shablon_b,1,v))
realChisla = sun_pol(progonka(shablon_b,2,v))
ishod_progonka = progonka(ishod_b,1,v)
ishod_progonka1 = progonka(ishod_b,2,v)

def Poiskporealpifag(vol,vol1,vol2,vol3,vol4):
    m=0
    n=0
    ch = 0
    ch1 = 0
    vrem = []
    vrem1 = []
    while m<len(vol):
        ch = ch + vol[m]
        ch1 = ch1 + vol1[m]
        if ch == vol2[0] and ch1 == vol3[0]:
            vrem.append(n)
            vrem1.append(m+1)
            ch = 0
            ch1 = 0
            n+=1
            m = n
        if ch > vol2[0] or ch1 > vol3[0]:

            ch = 0
            ch1 = 0
            n+=1
            m = n
        else:
            m+=1
    m = 0
    while m<len(vrem):
        d = vrem1[m]-vrem[m]
        m1 = 0
        while m1<d:
            q = vol4[vrem[m]+m1].upper()
            vol4[vrem[m]+m1] = q
            m1+=1
        m+=1
    resulkaknado = ' '.join(vol4)
    return resulkaknado

#print Poiskporealpifag(ishod_progonka,ishod_progonka1,pifagChisla,realChisla,ishod_b)
#sd = 'CHILD, I UNDERSTOOD AS A CHILD, I THOUGHT AS'
#sd = sd.lower()
s = 'clothe'
ishod = list(ishod)
s = list(s)
q = progonka(ishod,2,v)
w = progonka(s,2,v)

def pizdeckaknado(vol1,vol2,vol3):
    n =0
    b = []
    x = []
    c = 0
    while n<len(vol1):
        m = 0
        while m<len(vol2):
            if n >= len(vol1)-len(vol2):
                break
            if vol2[m]== vol1[n+m]:
                b.append(vol1[n+m])
                if m == len(vol2)-1 and len(b)-1 == m:
                    c = 1
                m+=1
                if vol1[n+m] == 0:
                    n+=1
            elif c == 1:
                c = 0
                for t in xrange(n-2,n+len(vol2)-1):
                    vb = vol3[t].upper()
                    vol3[t] = vb
            else:
                b = []
                m+=1
        n+=1
    result = ''.join(vol3)
    return result

print pizdeckaknado(q,w,ishod)


















