#!usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter

win = tkinter.Tk()
win.title("Ray")
win.geometry("700x500+350+150")


def funcPrintE():
    print(e.get())
    e.set("NO, I like you!")


btn = tkinter.Button(win, text="打印输入的内容", command=funcPrintE)  # 把lambda换成funcPrintE也一样 command=lambda:print(e.get())
btn.pack()

e = tkinter.Variable()
entry = tkinter.Entry(win, textvariable=e)
entry.pack()
# e.set('placeholder')
# print(e.get())


win.mainloop()
