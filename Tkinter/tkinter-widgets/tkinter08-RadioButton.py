#!usr/bin/env python
# -*- coding:utf-8 -*-


from tkinter import *

win = Tk()
win.title("Rayfengleixing")
win.geometry("700x500+350+150")


def updata():
	message = ""
	if r.get() == 1:
		message = "Money"
	if r.get() == 2:
		message = "Power"
	if r.get() == 3:
		message = "People"

	text.delete(0.0, END)
	text.insert(INSERT, message)

#绑定变量,以区分选中项, 一组单选框必须绑定同一个变量
r = IntVar() #r.get()的值就是前面给 value 赋的值, 但 r 是Int类型, 所以 value 的值也只能是数字
radio1 = Radiobutton(win, text="Money", value=1, variable=r, command=updata)
radio1.pack()
radio2 = Radiobutton(win, text="Power", value=2, variable=r, command=updata)
radio2.pack()
radio3 = Radiobutton(win, text="People", value=3, variable=r, command=updata)
radio3.pack()

text = Text(win, width=50, height=5)
text.pack()

win.mainloop()