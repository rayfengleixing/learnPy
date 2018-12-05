#!usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter

win = tkinter.Tk()
win.title("Ray")
win.geometry("700x500+350+150")
'''
entry 是一个输入控件，用于显示简单的文本内容,
show='*' 密码模式，其实'*'是什么，就显示什么，
如果想获取输入的值，就要绑定变量 e
'''
e = tkinter.Variable()
entry = tkinter.Entry(win, textvariable=e)
entry.pack()
e.set('placeholder')    # like placeholder
# print(e.get()) #获取值
# print(entry.get()) #同上，但是赋值只能用 e ，不能用 entry


win.mainloop()