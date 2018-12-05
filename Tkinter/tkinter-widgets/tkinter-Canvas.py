#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : tkinter-Canvas.py
# @Time    : 2018/10/29  17:39
# @Software: PyCharm
# @DESC    :

import tkinter as tk

win = tk.Tk()
win.title("Canvas")
win.geometry("700x500+250+150")

canvas = tk.Canvas(win, bg='blue', height=300, width=500)
img_file = tk.PhotoImage(file='../images/lye.gif')
img = canvas.create_image(10, 10, anchor='nw', image=img_file)

x0, y0, x1, y1 = 50, 50, 80, 80
line = canvas.create_line(x0, y0, x1, y1)
oval = canvas.create_oval(x0+50, y0+50, x1+50, y1+50, fill="yellow")    # 画圆
arc = canvas.create_arc(x0+100, y0+100, x1+100, y1+100, start=0, extent=180)    # 扇形
rect = canvas.create_rectangle(100, 30, 100+20, 30+20)  # 矩形

canvas.pack()


def move_it():
    canvas.move(img, 2, 2)  # 移动img, 每次x,y轴各两个像素


btn = tk.Button(win, text='move', command=move_it).pack()

win.mainloop()
