#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : tkinter-Bind.py
# @Time    : 2018/10/28  14:19
# @Software: PyCharm
# @DESC    : bind

"""
- bind 的用法：控件.bind(event, handler),其中event是tkinter已经定义好的的事件，handler是处理器，可以是一个处理函数，如果相关事件发生, handler 函数会被触发, 事件对象 event 会传递给 handler 函数
- 基本所有控件都能bind
- 常见event有：
    - 鼠标单击事件：鼠标左键点击为 <Button-1>, 鼠标中键点击为 <Button-2>, 鼠标右键点击为 <Button-3>, 向上滚动滑轮为 <Button-4>, 向下滚动滑轮为 <Button-5>.
    - 鼠标双击事件.：鼠标左键点击为 <Double-Button-1>, 鼠标中键点击为 <Double-Button-2>, 鼠标右键点击为 <Double-Button-3>.
    - 鼠标释放事件：鼠标左键点击为 <ButtonRelease-1>, 鼠标中键点击为 <ButtonRelease-2>, 鼠标右键点击为 <ButtonRelease-3>. 鼠标相对当前控件的位置会被存储在 event 对象中的 x 和 y 字段中传递给回调函数.
    - 鼠标移入控件事件：<Enter>
    - 获得焦点事件：<FocusIn>
    - 鼠标移出控件事件: <Leave>
    - 失去焦点事件:<FocusOut>
    - 鼠标按下移动事件：鼠标左键点击为 <B1-Motion>, 鼠标中键点击为 <B2-Motion>, 鼠标右键点击为 <B3-Motion>. 鼠标相对当前控件的位置会被存储在 event 对象中的 x 和 y 字段中传递给回调函数.
    - 键盘按下事件:<Key>，event中的keysym ,keycode,char都可以获取按下的键【其他想要获取值的也可以先看看event中有什么】
    - 键位绑定事件：<Return>回车键，<BackSpace>,<Escape>,<Left>,<Up>,<Right>,<Down>…….
    - 控件大小改变事件：<Configure>，新的控件大小会存储在 event 对象中的 width 和 height 属性传递. 有些平台上该事件也可能代表控件位置改变.
- Event中的属性：
    - widget：产生事件的控件
    - x, y：当前鼠标的位置
    - x_root, y_root：当前鼠标相对于屏幕左上角的位置，以像素为单位。
    - char：字符代码（仅限键盘事件），作为字符串。
    - keysym：关键符号（仅限键盘事件）。
    - keycode：关键代码（仅限键盘事件）。
    - num：按钮号码（仅限鼠标按钮事件）。
    - width, height：小部件的新大小（以像素为单位）（仅限配置事件）。
    - type：事件类型。
"""

from tkinter import *

root = Tk()
root.geometry("200x200")
text = Text(root)
text.pack()


def func(event):
    print(event)


def func_release(event):
    print("release")


# 单击
# text.bind("<Button-1>",func)
# root.bind("<Button-1>",func)
# 双击
# text.bind("<Double-Button-1>",func)
# 鼠标释放
# text.bind("<ButtonRelease-1>",func_release)
# 鼠标移入
# text.bind("<Enter>",func)
# 鼠标按住移动事件
# text.bind("<B1-Motion>",func)
# 键盘按下事件
# text.bind("<Key>",func)

# 键位绑定事件
# def func3(event):
#     print("你按下了回车!")
# text.bind("<Return>",func3)


# 实现的一个拖拽功能
def func4(event):
    # print(event)
    x = str(event.x_root)
    y = str(event.y_root)
    root.geometry("200x200+" + x + "+" + y)


text.bind("<B1-Motion>", func4)

root.mainloop()

"""
补充：如果想要传参，可以使用lambda:
"""
# text.bind("<Button-1>",lambda event:func(event,"hello"))
# a = ['a', 'b', 'c']
# text.bind("<Button-1>",lambda event:func(event,a))
# Result:
# <ButtonPress event state=Mod1 num=1 x=116 y=223> ['a', 'b', 'c']
