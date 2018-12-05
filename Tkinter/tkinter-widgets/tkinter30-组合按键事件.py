#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : tkinter30-组合按键事件.py
# @Time    : 2018/10/28  14:06
# @Software: PyCharm
# @DESC    : 组合按键事件

import tkinter

win = tkinter.Tk()
win.title("指定按键事件")
win.geometry("700x500+350+150")

'''
<Shift-Up>      Shift+Up
<Alt-Up>        Alt+Up
<Control-Up>    Ctrl+Up
<Control-A>     Ctrl+shift+a
'''


def func(e):
    print(e)
    print(e.keysym, e.keycode, e.char)


label = tkinter.Label(win, text="进来", width=30, height=5, fg="blue", bg="pink", font=("楷体", 20))
label.focus_set()  # 设置焦点,键盘事件必须获得控件的焦点才能响应
label.pack()

label.bind("<Control-A>", func)
label.bind("<Control-c>", func)

win.mainloop()
