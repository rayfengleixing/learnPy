#!usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("LLL")
win.geometry("700x500+350+150")

'''
表格数据
'''

table = ttk.Treeview(win)
table.pack(expand=1, fill=tkinter.BOTH)

table['columns'] = ("name", "age", "height", "weight")
table.column("name", width=100)
table.column("age", width=100)
table.column("height", width=100)
table.column("weight", width=100)

table.heading("name", text="姓名")
table.heading("age", text="年龄")
table.heading("height", text="身高")
table.heading("weight", text="体重")

table.insert("", 0, text="1", values=("张三", 21, 180, 180))
table.insert("", 1, text="2", values=("李四", 22, 177, 160))
table.insert("", 2, text="3", values=("王五", 24, 170, 140))
table.insert("", 3, text="4", values=("赵六", 23, 190, 190))





win.mainloop()