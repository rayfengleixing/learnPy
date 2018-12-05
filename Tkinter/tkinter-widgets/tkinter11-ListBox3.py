#!usr/bin/env python
# -*- coding:utf-8 -*-

from tkinter import *

win = Tk()
win.title("Rayfengleixing")
win.geometry("700x500+350+150")


def updata(e):
	pass


# EXTENDED 可以使 listbox 支持<Shift>和<Ctrl>的多选方式
lb = Listbox(win, selectmode=EXTENDED)
#lb.pack()

ll = ["zero", "one", "two", "three", "four", "five","zero", "one", "two", "three", "four", "five","zero", "one", "two", "three", "four", "five","zero", "one", "two", "three", "four", "five","zero", "one", "two", "three", "four", "five"]

for i in ll:
	lb.insert(END, i)

sc = Scrollbar(win)
sc.pack(side=RIGHT, fill=Y)
lb.configure(yscrollcommand=sc.set)
lb.pack(side=LEFT, fill=BOTH)
sc['command'] = lb.yview

win.mainloop()