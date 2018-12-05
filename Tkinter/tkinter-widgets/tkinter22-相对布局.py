#!usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter

win = tkinter.Tk()
win.title("相对布局")
win.geometry("700x500+350+150")


label1 = tkinter.Label(win, text="Python", bg="yellow")
label2 = tkinter.Label(win, text="Java", bg="red")
label3 = tkinter.Label(win, text="Php", bg="pink")
label4 = tkinter.Label(win, text="Mysql", bg="blue")


label1.pack(fill=tkinter.Y, side=tkinter.LEFT)
label2.pack(fill=tkinter.Y, side=tkinter.RIGHT)
label3.pack(fill=tkinter.X, side=tkinter.TOP)
label4.pack(fill=tkinter.X, side=tkinter.BOTTOM)


win.mainloop()
