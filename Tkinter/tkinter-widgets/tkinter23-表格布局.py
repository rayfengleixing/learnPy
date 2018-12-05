#!usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter

win = tkinter.Tk()
win.title("表格布局")
win.geometry("700x500+350+150")

label1 = tkinter.Label(win, text="Python", bg="yellow")
label2 = tkinter.Label(win, text="Java", bg="red")
label3 = tkinter.Label(win, text="Php", bg="pink")
label4 = tkinter.Label(win, text="Mysql", bg="blue")

label1.grid(row=0, column=0)
label2.grid(row=0, column=1)
label3.grid(row=1, column=1)
label4.grid(row=2, column=2)

win.mainloop()
