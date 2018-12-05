#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : 文件搜索.py
# @Time    : 2018/10/29  23:24
# @Software: PyCharm
# @DESC    : 给出正确的文件名,在指定目录下找到有该名称的文件,可双击打开查看

import fnmatch
import os
import tkinter as tk
import tkinter.messagebox
import tkinter.filedialog


def search_file():
    key_word = entry_word.get()
    file_type = '*.*'

    if not key_word:
        tk.messagebox.showinfo('!!!', "关键字不能为空!")
        return

    fn = tk.filedialog.askdirectory()  # 选择文件夹
    fn_list = os.walk(fn)  # 遍历目录

    list_box.delete(0, tk.END)

    for root, dirs, files in fn_list:
        # print(root)
        # print(dirs)
        # print(files)
        for i in fnmatch.filter(files, file_type):
            if key_word in i:   # 可以用 in 直接判断一个字符串是否包含于另一个字符串中
                # print("%s/%s" % (root, i))
                file_path = "%s/%s" % (root, i)
                list_box.insert(tk.END, file_path)


def click_in(e):
    try:
        index = list_box.curselection()[0]
        path = list_box.get(index)
        if not path:
            return

        window = tk.Tk()
        window.title("查看文件")
        window.geometry("800x600+250+100")
        text = tk.Text(window, width=60)
        text.pack(expand=1, fill=tk.BOTH)


        scroll = tk.Scrollbar(text)
        text.config(yscrollcommand=scroll.set)
        scroll.config(command=text.yview)
        scroll.pack(side=tk.RIGHT, fill=tk.Y)


        file_in_text = open(path, 'r', encoding='utf-8').read()
        text.insert(tk.END, file_in_text)

    except IndexError:
        pass


win = tk.Tk()
win.title("文件搜索")
win.geometry('+400+250')

lb_word = tk.Label(win, text="文件名: ").grid(row=0, column=0)
entry_word = tk.Entry(win)
entry_word.grid(row=0, column=1)

btn_search = tk.Button(win, text="选择目录", command=search_file)
btn_search.grid(row=0, column=2)

list_var = tk.StringVar()
list_box = tk.Listbox(win, width=70, listvariable=list_var)
list_box.bind("<Double-Button-1>", click_in)
list_box.grid(row=1, column=0, columnspan=3)

win.mainloop()
