#!usr/bin/python
#-*- coding:utf-8 -*-
from random import randint
class life(object):
    def __init__(self, vol):
        self.vol = vol
        self.q = len(vol[0])-1
        self.b = len(vol)-1
    def sosedi(self,vol1,vol2):
        self.sosed = 0
        for self.i in xrange(-1,2):
            for self.j in xrange(-1,2):
                if vol1+self.i == vol1 and vol2+self.j == vol2:
                    continue
                elif vol1 + self.i > self.q:
                    vol1 = 0
                    self.i = 0
                elif vol2+self.j > self.b:
                    vol2 = 0
                    self.j = 0
                if self.vol[vol1+self.i][vol2+self.j] != 0:
                    self.sosed += 1
        return self.sosed

def cikol(claas,masiv):
    nn = 0
    for n in masiv:
        mm = 0
        for ii in n:
            sosed1 = claas.sosedi(nn,mm)
            if ii == 1:
                if sosed1 < 2 or sosed1 > 3:
                    bb[nn][mm] = 0
            else:
                if sosed1 == 3:
                    bb[nn][mm] = 1
            mm+=1
        nn+=1
    return bb

a= [[randint(0,1) for i in range(0,5)] for j in range(0,5)]
bb = [[a[j][i] for i in range(0,5)] for j in range(0,5)]
#a = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,1,1,0,0],[0,0,0,1,1,1,0,0,0,0],[0,0,0,0,0,1,1,1,1,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
#bb = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,1,1,1,1,0,0],[0,0,0,1,1,1,0,0,0,0],[0,0,0,0,1,0,1,1,1,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
c = life(a)

from Tkinter import *
root = Tk()
var = StringVar()
var.set('Привет')
lab = Text(root, width = 100, height = 100, font = 14)
for n in a:
    lab.insert(END,'%s\n' %n)
#buttoms = Button()
#buttoms.pack()
lab.pack()
re = cikol(c,a)
def callback(event=None):
    global re
    lab.delete(1.0,END)
    for n in re:
        lab.insert(END,'%s\n' %n)
    c = life(re)
    re = cikol(c,re)
    lab.after(8000, callback)
#lab.after(500, callback)
lab.bind('<Button-1>', callback)
#buttom.bind('<Button-1>',)
root.mainloop()
