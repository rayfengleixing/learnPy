#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : tkinter28-响应特殊按键的键盘事件.py
# @Time    : 2018/10/28  13:37
# @Software: PyCharm
# @DESC    : 响应特殊按键的键盘事件

import tkinter

win = tkinter.Tk()
win.title("响应特殊按键的键盘事件")
win.geometry("700x500+350+150")

'''
<Return> 回车
<Cancel> Break键
<BackSpace> BackSpace键
<Tab> Tab键
<Shift_L> 左Shift键
<Alt_L> 左Alt键
<Control_L> 左Control键
<Pause> Pause键
<Caps_Lock> Caps_Lock键
<Escape> Escape键
<Prior> PageUp键
<Next> PageDown键
<End> End键
<Home> Home键
<Up> <Down> <Left> <Right> 上下左右
<Print> Print Screen键
<Insert> Insert键
<Delete> Delete键
<F1~F12> F1~F12键
<Num_Lock> Num_Lock键
<Scroll_Lock> Scroll_Lock键
<key> 任意键
'''


def func(e):
    print(e)
    print(e.keysym, e.keycode, e.char)


label = tkinter.Label(win, text="进来", width=30, height=5, fg="blue", bg="pink", font=("楷体", 20))
label.focus_set()  # 设置焦点,键盘事件必须获得控件的焦点才能响应
label.pack()

label.bind("<Shift_L>", func)

win.mainloop()
