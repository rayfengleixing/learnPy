#!usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter

win = tkinter.Tk()
win.title("LLL")
win.geometry("700x500+350+150")

'''
数值范围控件
from_=0, to=100, 同 scale
increment=5 步长
values 使控件只显示其中的值,而且和from_、to只能存其一
'''
def showNum():
	print(v.get())

#绑定变量,不然不能赋值和取值
v = tkinter.StringVar()
#sp = tkinter.Spinbox(win, values=(0, 2, 4, 6, 8))
sp = tkinter.Spinbox(win, from_=0, to=100, increment=5, textvariable=v, command=showNum)
sp.pack()

# 设置初始值
v.set(20)

# 取值
#print(v.get())
#tkinter.Button(win, text="PrintNum", command=showNum).pack()



win.mainloop()