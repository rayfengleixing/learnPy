#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : diaryWin.py
# @Time    : 2018/11/1  18:45
# @Software: PyCharm
# @DESC    : 日记本


from tkinter import *
from model import DiaryModel
import tkinter.messagebox
from toplevel import Toplv

win = Tk()

diary_list = None
s = ''


def new_file():
    title = entry_title.get()
    mood = entry_mood.get()
    weather = entry_weather.get()
    category = entry_category.get()
    content = textPad.get(1.0, END)

    if title.strip() != '' or mood.strip() != '' or weather.strip() != '' or \
            category.strip() != '' or content.strip() != '':
        jj = tkinter.messagebox.askyesnocancel('Warning',
                                               '请确定之前文件已经保存!')
        if jj:
            entry_title.delete(0, END)
            entry_mood.delete(0, END)
            entry_weather.delete(0, END)
            entry_category.delete(0, END)
            textPad.delete(1.0, END)


def save_file():
    title = entry_title.get()
    mood = entry_mood.get()
    weather = entry_weather.get()
    category = entry_category.get()
    content = textPad.get(1.0, END)

    if title.strip() == '':
        tkinter.messagebox.showinfo('Sorry!', '标题不能为空!')
    elif mood.strip() == '':
        tkinter.messagebox.showinfo('Sorry!', '心情不能为空!')
    elif weather.strip() == '':
        tkinter.messagebox.showinfo('Sorry!', '天气不能为空!')
    elif category.strip() == '':
        tkinter.messagebox.showinfo('Sorry!', '类型不能为空!')
    elif content.strip() == '':
        tkinter.messagebox.showinfo('Sorry!', '内容不能为空!')
    else:
        sure = tkinter.messagebox.askyesno('!!!', '确定要保存当前所有内容吗?')
        if sure:
            model = DiaryModel()
            model_create = model.create_diary(title=title, mood=mood,
                                              weather=weather,
                                              category=category,
                                              content=content)

            if model_create:
                print("保存成功!")
            else:
                print("保存失败!")


def show_end(show_all_top, diary_list, model):
    ln = 0
    for i in diary_list:
        # i['id']
        show_all_top.table.insert('', ln, values=(
        i['id'], i['title'], i['mood'], i['weather'], i['category'],
        i['c_time']))
        ln += 1

    def onDBClick(e):
        item = show_all_top.table.selection()[0]
        # print(table.item(item, 'values')[0])
        id = show_all_top.table.item(item, 'values')[0]
        l = model.get_info_by_id(id)
        title_var.set(l['title'])
        mood_var.set(l['mood'])
        weather_var.set(l['weather'])
        category_var.set(l['category'])
        textPad.delete(1.0, END)
        textPad.insert(1.0, l['content'])

        show_all_top.destroy()

    show_all_top.table.bind("<Double-1>", onDBClick)


def show_by_date():
    global diary_list
    global s
    s = 'date'
    model = DiaryModel()
    diary_list = model.get_info_by_date()

    return diary_list


def show_by_category():
    global diary_list
    global s
    s = 'category'
    model = DiaryModel()
    diary_list = model.get_info_by_category()

    return diary_list


def show_all():
    global diary_list
    global s
    s = 'all'
    model = DiaryModel()
    diary_list = model.get_diary_list()

    return diary_list


def show_list():
    global diary_list
    list_pad = Toplv(win)


win.title("新建日记")
win.geometry("800x600+250+50")
win.resizable(0, 0)

# Menu Bar
menu_bar = Menu(win)
win.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=False)
file_menu.add_command(label='新建', command=new_file)
file_menu.add_command(label='保存', command=save_file)
file_menu.add_separator()
file_menu.add_command(label='退出', command=lambda: win.quit())
menu_bar.add_cascade(label='文件', menu=file_menu)

view_menu = Menu(menu_bar, tearoff=False)
view_menu.add_command(label='显示所有', command=show_list)
menu_bar.add_cascade(label='查看', menu=view_menu)

about_menu = Menu(menu_bar, tearoff=False)
about_menu.add_command(label='作者')
about_menu.add_command(label='版权')
menu_bar.add_cascade(label='关于', menu=about_menu)

frm = Frame(win)
label_title = Label(frm, text=' 标题:', font=("楷体", 10))
label_title.pack(side=LEFT)
title_var = StringVar()
entry_title = Entry(frm, width=40, font=("楷体", 12), textvariable=title_var)
entry_title.pack(side=LEFT)
label_mood = Label(frm, text=' 心情:', font=("楷体", 12))
label_mood.pack(side=LEFT)
mood_var = StringVar()
entry_mood = Entry(frm, width=10, font=("楷体", 12), textvariable=mood_var)
entry_mood.pack(side=LEFT)
label_weather = Label(frm, text=' 天气:', font=("楷体", 12))
label_weather.pack(side=LEFT)
weather_var = StringVar()
entry_weather = Entry(frm, width=10, font=("楷体", 12),
                      textvariable=weather_var)
entry_weather.pack(side=LEFT)
label_category = Label(frm, text=' 类型:', font=("楷体", 12))
label_category.pack(side=LEFT)
category_var = StringVar()
entry_category = Entry(frm, width=10, font=("楷体", 12),
                       textvariable=category_var)
entry_category.pack(side=LEFT)
frm.pack(expand=NO, fill=X)

# Text Pad
textPad = Text(win, undo=True, font=("楷体", 16))
textPad.pack(expand=YES, fill=BOTH)

scroll = Scrollbar(textPad)
textPad.config(yscrollcommand=scroll.set)
scroll.config(command=textPad.yview)
scroll.pack(side=RIGHT, fill=Y)

win.mainloop()
