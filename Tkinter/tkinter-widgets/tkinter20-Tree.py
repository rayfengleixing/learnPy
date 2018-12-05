#!usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter
from tkinter import ttk

win = tkinter.Tk()
win.title("LLL")
win.geometry("700x500+350+150")

'''
树状数据
'''

tree = ttk.Treeview(win)
tree.pack()

# 一级树枝
treeOne1 = tree.insert("", 0, "China", text="中国", values=("CHN"))
treeOne2 = tree.insert("", 1, "British", text="英国", values=("UK"))
treeOne3 = tree.insert("", 2, "American", text="美国", values=("USA"))

# 二级树枝
treeTwo1 = tree.insert(treeOne1, 0, "Xi'an", text="西安", values=("XIAN"))
treeTwo2 = tree.insert(treeOne1, 1, "XianYang", text="咸阳", values=("XY"))
treeTwo3 = tree.insert(treeOne1, 2, "YongShou", text="永寿", values=("YS"))
treeTwo4 = tree.insert(treeOne2, 0, "London", text="伦敦", values=("LONDON"))
treeTwo5 = tree.insert(treeOne3, 0, "Los Angeles", text="洛杉矶", values=("LA"))

win.mainloop()
