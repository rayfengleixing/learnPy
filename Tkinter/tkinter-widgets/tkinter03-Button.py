# -*- coding:utf-8 -*-

import tkinter

win = tkinter.Tk()
win.title("Ray")
win.geometry("700x500+350+150")

def func():
	print("Ray like Luyu!")

btn1 = tkinter.Button(win, text="点我", command=func, width=10, height=2)
btn1.pack()
#lambda 匿名函数 对比btn1、btn2
btn2 = tkinter.Button(win, text="戳我", command=lambda:print("Fuck!"))
btn2.pack()
#看command 一目了然
btn3 = tkinter.Button(win, text="摁我", command=win.quit)
btn3.pack()






win.mainloop()