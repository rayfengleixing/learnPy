#!/usr/bin/env python
# -*- coding:utf-8 -*-
from tkinter import *
def donothing():
    filewin=Toplevel(root)
    button=Button(filewin,text="hi 这是菜单响应代码段")
    button.pack()

root=Tk()
root.title("记事本")
root.geometry("800x500")
menubar=Menu(root)
filemenu = Menu(menubar, tearoff=0)

filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="新建",accelerator="Ctrl+N",command=donothing)
filemenu.add_command(label="打开",accelerator="Ctrl+O",command=donothing)
filemenu.add_command(label="保存",accelerator="Ctrl+S",command=donothing)
filemenu.add_command(label="另存为",accelerator="Ctrl+Shift+S",command=donothing)
filemenu.add_separator()
filemenu.add_command(label="页面设置",accelerator="U",command=donothing)
filemenu.add_command(label="打印",accelerator="Ctrl+P",command=donothing)
filemenu.add_separator()
filemenu.add_command(label="退出",accelerator="X",command=root.quit)
menubar.add_cascade(label="文件",menu=filemenu)

editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=donothing)
editmenu.add_separator()
editmenu.add_command(label="Cut", command=donothing)
editmenu.add_command(label="Copy", command=donothing)
editmenu.add_command(label="Paste", command=donothing)
editmenu.add_command(label="Delete", command=donothing)
editmenu.add_command(label="Select All", command=donothing)
menubar.add_cascade(label="Edit", menu=editmenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=donothing)
helpmenu.add_command(label="About...", command=donothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)

txt=Text(root,undo=True)
txt.pack(expand=YES,fill=BOTH)

scl=Scrollbar(txt)
txt.config(yscrollcommand=scl.set)
scl.config(command=txt.yview())
scl.pack(side=RIGHT,fill=Y)

statusbar=Label(root,text="行 1 column 1",bg="#fff",fg="#00c",relief=SUNKEN,anchor=E)

statusbar.pack(side=BOTTOM,fill=X)



if __name__ == "__main__":
    mainloop()
