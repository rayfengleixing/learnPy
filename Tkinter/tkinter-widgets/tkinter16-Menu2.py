#!usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter

win = tkinter.Tk()
win.title("LLL")
win.geometry("700x500+350+150")
'''
鼠标右键菜单
'''

menubar = tkinter.Menu(win)

menu = tkinter.Menu(menubar, tearoff=False)

ll = ["Python", "Java", 'Mysql', 'C++', 'Php']
for i in ll:
	menu.add_command(label=i)

menubar.add_cascade(label="Lanauage", menu=menu)

def showMenu(event):
	menubar.post(event.x_root, event.y_root)

win.bind("<Button-3>", showMenu)



win.mainloop()