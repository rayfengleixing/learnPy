#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : tkinter-MessageBox.py
# @Time    : 2018/10/29  17:02
# @Software: PyCharm
# @DESC    :

import tkinter as tk
import tkinter.messagebox
# 要使用messagebox,还要单独导入

win = tk.Tk()
win.title("MessageBox")
win.geometry("300x300")


def hit_me():
    # tk.messagebox.showinfo(title='', message='')        # 提示信息对话窗
    # tk.messagebox.showwarning(title='', message='')     # 提出警告对话窗
    # tk.messagebox.showerror(title='', message='')       # 提出错误对话窗
    # tk.messagebox.askquestion(title='', message='')     # 询问选择对话窗 return 'yes' or 'no'
    # tk.messagebox.askyesno(title='', message='')        # return True or False
    # tk.messagebox.askretrycancel(title='', message='')  # return True or False
    # tk.messagebox.askokcancel(title='', message='')     # return True or False
    tk.messagebox.askyesnocancel(title='Hi!', message='是不是不爱了?')  # return True or False or None


tk.Button(win, text="hit me", command=hit_me).pack()

win.mainloop()
