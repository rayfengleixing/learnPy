#!usr/bin/env python
# -*- coding:utf-8 -*-

import tkinter

win = tkinter.Tk()
win.title("LLL")
win.geometry("700x500+350+150")

'''
供用户通过拖拽指示器来改变变量的值,类似音乐播放器的音量调节
from 是关键字,所以前面要加下划线
orient 标定方向, horizontal 水平的, vertical 竖直的
tickinterval 显示进度条的刻度, 具体看效果就很明白
'''
scale = tkinter.Scale(win, from_=0, to=1000, orient=tkinter.HORIZONTAL, tickinterval=100, length=300)
scale.pack()

# 设置初始值
scale.set(500)


# 获取当前值
def showNum():
	print(scale.get())

tkinter.Button(win, text="按钮", command=showNum).pack()



win.mainloop()