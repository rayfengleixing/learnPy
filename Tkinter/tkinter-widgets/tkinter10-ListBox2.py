#!usr/bin/env python
# -*- coding:utf-8 -*-

from tkinter import *

win = Tk()
win.title("Rayfengleixing")
win.geometry("700x500+350+150")


def updata(e):
	print(lb.get(lb.curselection()))

# SINGLE 模式与 BROWSE 的区别是, 这个模式不支持鼠标按住时,移动选中选项
lbv = StringVar()
lb = Listbox(win, selectmode=SINGLE, listvariable=lbv)
lb.pack()

ll = ["zero", "one", "two", "three", "four", "five"]

for i in ll:
	lb.insert(END, i)

# 设置选项
#lbv.set(("1", "2", "3", "4"))

# <Double-Button-1> 双击鼠标左键
lb.bind("<Double-Button-1>", updata)


win.mainloop()