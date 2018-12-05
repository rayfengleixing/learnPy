#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : tkinter27-响应所有按键的键盘事件.py
# @Time    : 2018/10/28  12:54
# @Software: PyCharm
# @DESC    : 响应所有按键的键盘事件

import tkinter

win = tkinter.Tk()
win.title("响应所有按键的键盘事件")
win.geometry("700x500+350+150")

'''
<Key> 响应所有按键的键盘事件
'''


def func(e):
    print(e)
    # keysym 按键所对应的键盘符号
    print(e.keysym, e.keycode, e.char)


label = tkinter.Label(win, text="进来", width=30, height=5, fg="blue", bg="pink", font=("楷体", 20))
label.focus_set()  # 设置焦点,键盘事件必须获得控件的焦点才能响应
label.pack()

label.bind("<Key>", func)

# win.bind("<Key>", func)   # 直接给 win 绑定事件也可以,不用获取焦点


win.mainloop()
