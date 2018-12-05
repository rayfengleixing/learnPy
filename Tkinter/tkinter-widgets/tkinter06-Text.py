#!usr/bin/env python
# -*- coding:utf-8 -*-

#import tkinter
from tkinter import * #这样写，下面就不用老是写 tkinter.*** 了，直接 ***

win = Tk()
win.title("Ray")
win.geometry("700x500+350+150")

def func():
	str = '''
#!usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter

win = Tk()
win.title("Ray")
win.geometry("700x500+350+150")

def func():
	str = '***'
	text.insert(INSERT, str)
	
btn = Button(win, text="Fuck me", command=func)
btn.pack()

#width 显示的列数		height 行数
#创建滚动条
scroll = Scrollbar()
text = Text(win, font=('楷体', 16))
scroll.pack(side=RIGHT, fill=Y) #放在窗体右侧，填充Y轴方向
text.pack(side=LEFT, fill=Y)
#两者关联起来
scroll.config(command=text)

win.mainloop()
	'''
	text.insert(INSERT, "I wanna fuck Renxinling")
	#print("I wanna fuck Renxinling")
	print(text.get('0.0', END))
	
btn = Button(win, text="Fuck me", command=func)
btn.pack()

#width 显示的列数		height 行数
#创建滚动条
scroll = Scrollbar()
text = Text(win, font=('楷体', 16))
#放在窗体右侧，填充Y轴方向
scroll.pack(side=RIGHT, fill=Y) 
text.pack(side=LEFT, fill=Y)
#两者关联起来
#滚动条控制text
scroll.config(command=text.yview)
#滚动条跟随text，就是text控制滚动条
text.config(yscrollcommand=scroll.set)


win.mainloop()