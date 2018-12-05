#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : toplevel.py
# @Time    : 2018/11/2  17:48
# @Software: PyCharm
# @DESC    :
from tkinter import *
from tkinter import ttk


class Toplv(Toplevel):
    __instance = None
    __init__flag = False

    def __new__(cls, master=None):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self, master=None):
        if not Toplv.__init__flag:
            super().__init__(master)
            self.title('Show All')
            self.geometry("700x500+300+100")
            # self.layout(func1=None, func2=None, func3=None)
            self.list = None
            Toplv.__init__flag = True

    def layout(self, func1=None, func2=None, func3=None):
        # 搜索栏
        self.select_line = Frame(self)

        self.btn_find_all = Button(self.select_line, text='显示全部', padx=1,
                                   command=func1)
        self.btn_find_all.pack(side=LEFT)

        self.time_var1 = StringVar()
        self.entry_time1 = Entry(self.select_line, textvariable=self.time_var1)
        self.entry_time1.pack(side=LEFT)
        self.btn_time = Button(self.select_line, text='<按日期>', padx=1,
                               command=func2)
        self.btn_time.pack(side=LEFT)
        self.time_var2 = StringVar()
        self.entry_time2 = Entry(self.select_line, textvariable=self.time_var2)
        self.entry_time2.pack(side=LEFT)

        self.type_var = StringVar()
        self.entry_type = Entry(self.select_line, textvariable=self.type_var)
        self.entry_type.pack(side=RIGHT)
        self.btn_type = Button(self.select_line, text='按类型>', padx=1,
                               command=func3)
        self.btn_type.pack(side=RIGHT)

        self.select_line.pack(expand=0, fill=X)

        # 列表面板
        self.table = ttk.Treeview(self, show='headings')
        self.table.pack(expand=1, fill=BOTH)

        self.scroll = Scrollbar(self.table)
        self.table.config(yscrollcommand=self.scroll.set)
        self.scroll.config(command=self.table.yview)
        self.scroll.pack(side=RIGHT, fill=Y)

        self.table['columns'] = (
            'id', 'title', 'mood', 'weather', 'category', 'time')
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
