#!usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter

win = tkinter.Tk()
win.title("LLL")
win.geometry("700x500+350+150")


label1 = tkinter.Label(win, text="Python", bg="yellow")
label2 = tkinter.Label(win, text="Java", bg="red")
label3 = tkinter.Label(win, text="Php", bg="pink")
label4 = tkinter.Label(win, text="Mysql", bg="blue")

# 绝对布局
label1.place(x=10, y=10)
label2.place(x=10, y=50)
label3.place(x=100, y=100)
label4.place(x=200, y=100)







win.mainloop()