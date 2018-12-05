#!usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter

win = tkinter.Tk()
win.title("LLL")
win.geometry("700x500+350+150")
'''
顶层菜单

'''
# 创建一个菜单栏
menubar = tkinter.Menu(win)
win.config(menu=menubar)
# 菜单选项
menu1 = tkinter.Menu(menubar, tearoff=False)


# 给菜单选项的具体项添加功能
def func():
    pass


# 给菜单选项添加内容
ll = ["Python", "Java", 'Mysql', 'C++', 'Php', 'Exit']
for i in ll:
    if i == "Exit":
        menu1.add_separator()
        menu1.add_command(label=i, command=lambda: win.quit())
    # 这个也可以
    # menu1.add_command(label=i, command=win.quit)
    else:
        menu1.add_command(label=i, command=func)
# 往菜单栏里添加菜单选项
menubar.add_cascade(label="Language", menu=menu1)

menu2 = tkinter.Menu(menubar, tearoff=False)
menu2.add_command(label="Ray")
menu2.add_command(label="Yu")
menu2.add_command(label="Cong")
menubar.add_cascade(label="Color", menu=menu2)

win.mainloop()
