#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : toplv.py
# @Time    : 2018/11/4  22:55
# @Software: PyCharm
# @DESC    :

from tkinter import *
from tkinter import ttk


class Toplv(Toplevel):
    def __init__(self, master=None):
        super().__init__(master)
        self.title("全部显示")
        self.geometry("600x400+350+150")
        self.table = None
        self.scroll = None
        self.layout()

    def layout(self):
        self.table = ttk.Treeview(self, show='headings')
        self.table.pack(expand=1, fill=BOTH)

        self.scroll = Scrollbar(self.table)
        self.table.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.table.yview)
        self.scroll.pack(side=RIGHT, fill=Y)

        self.table['columns'] = ('id', 'title', 'mood', 'weather', 'category',
                                 'time')
        self.table.column('id', width=10)
        self.table.column('title', width=100)
        self.table.column('mood', width=20)
        self.table.column('weather', width=20)
        self.table.column('category', width=20)
        self.table.column('time', width=100)

        self.table.heading('id', text='Id')
        self.table.heading('title', text='标题')
        self.table.heading('mood', text='心情')
        self.table.heading('weather', text='天气')
        self.table.heading('category', text='类型')
        self.table.heading('time', text='时间')
