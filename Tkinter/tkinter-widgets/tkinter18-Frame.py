#!usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter

win = tkinter.Tk()
win.title("LLL")
win.geometry("700x500+350+150")
'''
框架、容器

'''
frm = tkinter.Frame(win)
frm.pack()

frmLeft = tkinter.Frame(frm)
frmLeft.pack(side=tkinter.LEFT)
tkinter.Label(frmLeft, text="左上", bg="pink").pack(side=tkinter.TOP)
tkinter.Label(frmLeft, text="左下", bg="blue").pack(side=tkinter.TOP)

frmRight = tkinter.Frame(frm)
frmRight.pack(side=tkinter.RIGHT)
tkinter.Label(frmRight, text="右上", bg="red").pack(side=tkinter.TOP)
tkinter.Label(frmRight, text="右下", bg="green").pack(side=tkinter.TOP)






win.mainloop()