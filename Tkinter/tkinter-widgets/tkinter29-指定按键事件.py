#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : tkinter29-指定按键事件.py
# @Time    : 2018/10/28  14:00
# @Software: PyCharm
# @DESC    : 制定按键事件

import tkinter

win = tkinter.Tk()
win.title("指定按键事件")
win.geometry("700x500+350+150")

'''
a   字母a
b   字母b
1   数字1
<KeyPress-a>    按下时
<KeyRelease-a>  释放时
A   shift+a
B   shift+b
'''


def func(e):
    print(e)
    print(e.keysym, e.keycode, e.char)


label = tkinter.Label(win, text="进来", width=30, height=5, fg="blue", bg="pink", font=("楷体", 20))
label.focus_set()  # 设置焦点,键盘事件必须获得控件的焦点才能响应
label.pack()

label.bind("a", func)

win.mainloop()
