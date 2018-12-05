#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : tkinter25-鼠标移动事件.py
# @Time    : 2018/10/28  12:21
# @Software: PyCharm
# @DESC    : 鼠标移动事件

import tkinter

win = tkinter.Tk()
win.title("鼠标移动事件")
win.geometry("700x500+350+150")

'''
<Enter> 当鼠标 移入 控件时事件发生
<Leave> 当鼠标 移出 ......
<B1-Motion> 按住左键拖动
<B3-Motion> 右键拖动
'''


def func(e):
    print(e.x, e.y)


label = tkinter.Label(win, text="进来", width=30, height=5, fg="blue", bg="pink", font=("楷体", 20))
label.pack()

label.bind("<Enter>", func)
label.bind("<Leave>", func)
label.bind("<B3-Motion>", func)

win.mainloop()
