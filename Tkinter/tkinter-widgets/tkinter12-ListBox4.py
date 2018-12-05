#!usr/bin/env python
# -*- coding:utf-8 -*-

from tkinter import *

win = Tk()
win.title("Rayfengleixing")
win.geometry("700x500+350+150")

# MULTIPLE 支持多选
lb = Listbox(win, selectmode=MULTIPLE)
lb.pack()

ll = ["zero", "one", "two", "three", "four", "five"]

for i in ll:
	lb.insert(END, i)

win.mainloop()