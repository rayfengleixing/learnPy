#!usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("LLL")
win.geometry("700x500+350+150")
'''
下拉框控件
这个最好多导入 ttk 库
'''
cv = tkinter.StringVar()
cb = ttk.Combobox(win, textvariable=cv)
cb.pack()

cb['value'] = ("HeiLongjiang", 'JiLin', 'LiaoNing')
# 设置默认值
cb.current(0)

# 绑定事件
def func(e):
	# 有些控件可以直接 get(), 有些不能
	# 不能的就需要绑定变量, 能 get() 的也可以绑定变量获取 
	print(cb.get())
	print(cv.get())
	
	
cb.bind("<<ComboboxSelected>>", func)



win.mainloop()