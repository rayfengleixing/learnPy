#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : tkinter-Command.py
# @Time    : 2018/10/28  14:16
# @Software: PyCharm
# @DESC    : command

"""
command 是控件中的一个参数，如果使得 command= 函数，那么点击控件的时候将会触发函数
能够定义command 的常见控件有: Button、Menu...
调用函数时，默认是没有参数传入的，如果要强制传入参数，可以考虑使用 lambda
"""

from tkinter import *

root = Tk()


def prt():
    print("hello")


def func1(*args, **kwargs):
    print(*args, **kwargs)


hello_btn = Button(root, text="hello", command=prt)  # 演示
hello_btn.pack()

args_btn = Button(root, text="获知是否button事件默认有参数", command=func1)  # 获知是否有参数,结果是没有
args_btn.pack()

btn1 = Button(root, text="传输参数", command=lambda: func1("running"))  # 强制传输参数
btn1.pack()

root.mainloop()
