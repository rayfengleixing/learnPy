#!usr/bin/env python
# -*- coding:utf-8 -*-

from tkinter import *

win = Tk()
win.title("Rayfengleixing")
win.geometry("700x500+350+150")


def updata():
	message = ""
	if hobby1.get() == True:
		message += "Money  "
	if hobby2.get() == True:
		message += "Power  "
	if hobby3.get() == True:
		message += "People  "

	#0.0表示下标的开始, END同理
	text.delete(0.0, END)
	text.insert(INSERT, message)

#布尔变量,判断是否选中用
hobby1 = BooleanVar()
check1 = Checkbutton(win, text="Money", variable=hobby1, command=updata)
check1.pack()

hobby2 = BooleanVar()
check2 = Checkbutton(win, text="Power", variable=hobby2, command=updata)
check2.pack()

hobby3 = BooleanVar()
check3 = Checkbutton(win, text="People", variable=hobby3, command=updata)
check3.pack()

text = Text(win, width=50, height=5)
text.pack()


win.mainloop()