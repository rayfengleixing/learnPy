#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : note.py
# @Time    : 2018/10/31  21:37
# @Software: PyCharm
# @DESC    : 按视频仿写记事本

from tkinter.filedialog import *
from tkinter.messagebox import *
from tkinter import *
import os

filename = ''

def author():
    showinfo("作者信息", '作者不就是我了,自己对自己有什么不知道的!\n这东西别人又看不见!!!')

def about():
    showinfo('版权信息.copyright', '本软件的所有权并不归我自己所有.\n因为是网上看视频抄的!')

def openfile():
    global filename
    # 这是打开文件的那个窗口, filename是被打开文件的完整路径
    filename = askopenfilename(defaultextension=".txt")
    if '' == filename:
        filename = None
    else:
        # os.path.basename(filename) 当前文件名
        win.title('FileName: ' + os.path.basename(filename))
        textPad.delete(1.0, END)
        f = open(filename, 'r')
        textPad.insert(1.0, f.read())
        f.close()

def new():
    print(textPad.get(1.0, END))
    global filename
    content = textPad.get(1.0, END)
    # print(len(content)) # 1
    if len(content) > 1:
        showinfo(message="file not save!")
    else:
        win.title("UnNamed.txt")
        filename = None
        textPad.delete(1.0, END)

def save_file():
    global filename
    # print(filename + 'save file')
    try:
        f = open(filename, 'w')
        msg = textPad.get(1.0, END)
        f.write(msg)
        f.close()
    except:
        save_as()

def save_as():
    # 另存为窗口, f 为文件完整路径
    f = asksaveasfilename(initialfile="UnNamed.txt", defaultextension=".txt")
    global filename
    # print(filename + 'save_as filename')
    try:
        filename = f
        fh = open(f, 'w')
        msg = textPad.get(1.0, END)
        fh.write(msg)
        fh.close()
        win.title('FileName: ' + os.path.basename(f))
    except:
        pass

def cut():
    textPad.event_generate('<<Cut>>')

def copy():
    textPad.event_generate('<<Copy>>')

def paste():
    textPad.event_generate('<<Paste>>')

def redo():
    textPad.event_generate('<<Redo>>')

def undo():
    textPad.event_generate('<<Undo>>')

def find():
    top_find = Toplevel(win)
    top_find.geometry("300x30+450+170")

    find_label = Label(top_find, text="Words")
    find_label.grid(row=0, column=0, padx=5)

    find_entry = Entry(top_find, width=27)
    find_entry.grid(row=0, column=1, padx=5)

    find_btn = Button(top_find, text='Find')
    find_btn.grid(row=0, column=2)

def select_all():
    textPad.tag_add(1.0, END)

win = Tk()
win.title('UnNamed')
win.geometry('700x500+350+100')

menu_bar = Menu(win)
win.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=False)  # 把 tearoff 去掉试试,就知道它有什么用了
file_menu.add_command(label='New', accelerator='Ctrl + N', command=new)
file_menu.add_command(label='Open', accelerator='Ctrl + O', command=openfile)
file_menu.add_command(label='Save', accelerator='Ctrl + S', command=save_file)
file_menu.add_command(label='SaveAs', accelerator='Ctrl + Shift + S', command=save_as)
file_menu.add_separator()
file_menu.add_command(label='Exit', accelerator='Alt + F4', command=lambda :win.quit())
menu_bar.add_cascade(label='File', menu=file_menu)

edit_menu = Menu(menu_bar, tearoff=False)
edit_menu.add_command(label='Undo', accelerator='Ctrl + Z', command=undo)
edit_menu.add_command(label='Redo', accelerator='Ctrl + Y', command=redo)
edit_menu.add_separator()
edit_menu.add_command(label='Cut', accelerator='Ctrl + X', command=cut)
edit_menu.add_command(label='Copy', accelerator='Ctrl + C', command=copy)
edit_menu.add_command(label='Paste', accelerator='Ctrl + V', command=paste)
edit_menu.add_separator()
edit_menu.add_command(label='Find', accelerator='Ctrl + F', command=find)
edit_menu.add_command(label='SelectAll', accelerator='Ctrl + A', command=select_all)
menu_bar.add_cascade(label='Edit', menu=edit_menu)

about_menu = Menu(menu_bar, tearoff=False)
about_menu.add_command(label='Author', command=author)
about_menu.add_command(label='About', command=about)
menu_bar.add_cascade(label='About', menu=about_menu)

# Status line 未实现
status_line = Label(win, text='Ln20', bd=1, relief=SUNKEN, anchor=W)
status_line.pack(side=BOTTOM, fill=X)

# Line number 未实现
ln = Label(win, width=2, bg='antique white')
ln.pack(side=LEFT, fill=Y)

textPad = Text(win, undo=True)
textPad.pack(expand=YES, fill=BOTH)

# win.bind('<Control-o>', openfile)
# win.bind('<Control-n>', new)

scroll = Scrollbar(textPad)
textPad.config(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT, fill=Y)

win.mainloop()
