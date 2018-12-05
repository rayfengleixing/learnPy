#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : tkinter-Protocol.py
# @Time    : 2018/10/28  14:31
# @Software: PyCharm
# @DESC    : protocol

"""
- protocol的使用：控件.protocol(protocol，handler)，其中控件为窗口对象(Tk,Toplevel)
- 常见protocol有：
    - WM_DELETE_WINDOW：最常用的协议称为WM_DELETE_WINDOW，用于定义用户使用窗口管理器\
    明确关闭窗口时发生的情况。如果使用自己的handler来处理事件的话，这时候窗口将不会自动执行关闭
    - WM_TAKE_FOCUS，WM_SAVE_YOURSELF：[这两个不知道什么来的。]
    - 更多需参考ICCCM文档
- 注意：要留心协议的写法，在作为字符串填入时不要加多余的空格
"""

from tkinter import *
import tkinter.messagebox

root = Tk()
root.geometry("200x200")


def func1():
    if tkinter.messagebox.askyesno("关闭窗口", "确认关闭窗口吗"):
        root.destroy()


root.protocol("WM_DELETE_WINDOW", func1)

root.mainloop()
