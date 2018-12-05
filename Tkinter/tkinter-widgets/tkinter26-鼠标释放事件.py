#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : tkinter26-鼠标释放事件.py
# @Time    : 2018/10/28  12:36
# @Software: PyCharm
# @DESC    : 鼠标释放事件

import tkinter

win = tkinter.Tk()
win.title("鼠标释放事件")
win.geometry("700x500+350+150")

'''
<ButtonRelease-1> 当释放鼠标 左键 时事件发生
<ButtonRelease-3> 当释放鼠标 右键 时事件发生
'''


def func(e):
    print(e.x, e.y)


label = tkinter.Label(win, text="进来", width=30, height=5, fg="blue", bg="pink", font=("楷体", 20))
label.pack()

label.bind("<ButtonRelease-1>", func)

win.mainloop()
