#!usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter

win = tkinter.Tk()
win.title("鼠标点击事件")
win.geometry("700x500+350+150")

'''
<Button-1> 1、2、3分别表示鼠标的左中右键

<1> = <Button-1> =<ButtonPress-1>
<2> = <Button-2> = <ButtonPress-2>
<3> = <Button-3> =<ButtonPress-3>

<Double-Button-1> 鼠标双击事件
<Triple-Button-1> 鼠标三击事件
<Enter> 当鼠标 移入 控件时事件发生
<Leave> 当鼠标 移出 ......
'''


def func(event):
    # num1,2,3对应鼠标左中右键, x,y对应鼠标点击时所在容器中的坐标
    print(event.num, event.x, event.y)
    # x_root,y_root 对应鼠标点击时在屏幕中的坐标
    print(event.x_root, event.y_root)


btn = tkinter.Button(win, text="左键点我")
btn.pack()

# <1> = <Button-1> =<ButtonPress-1>
btn.bind("<1>", func)

win.mainloop()
