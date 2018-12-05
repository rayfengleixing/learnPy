# -*- coding:utf-8 _*_
import tkinter

# 创建主窗口
win = tkinter.Tk()
# 设置标题
win.title("Label控件")
# 大小和位置(宽x高+X+Y)
win.geometry("700x500+350+150")
'''
Label标签容器（类似<span>标签）
width代表多少列，
height代表多少行，
wraplength换行的宽度，用值不确定, 
justify和align一个意思
anchor显示的位置 center n e w s 东南西北的首字母，也可以ne se nw sw
'''
label = tkinter.Label(win, text="Label!", bg="pink", fg="blue", font=("楷体", 20), width=30, height=10, wraplength=200,
                      anchor="center")

# 显示出来
label.pack()

win.mainloop()
