#!usr/bin/env python
# -*- coding:utf-8 -*-

from tkinter import *

win = Tk()
win.title("Rayfengleixing")
win.geometry("700x500+350+150")

lb = Listbox(win, selectmode=BROWSE)
lb.pack()

ll = ["one", "two", "three", "four"]

for i in ll:
    # 写 END 是在最后面加入,就是顺序添加
    lb.insert(END, i)
# ACTIVE 就是往最前面添加 
lb.insert(ACTIVE, "zero")
# 将列表会当成一个元素添加进去
lb.insert(END, ["five", "six", "seven"])

# 删除	参数1位开始的索引, 参数2为结束的索引, 如果不指定参数2, 则只删除参数1处的内容
# 第一个元素的下标为 0 , 所以此处删除的是第 2 到第 4 的元素
# lb.delete(1, 3)

# 选中	也有两个参数, 同上, 要么选范围, 要么单选
lb.select_set(1, 4)
# lb.select_set(2)

# 取消选中	也是两个参数, 同上
lb.select_clear(2, 3)

print(lb.size())  # 6
print(lb.get(2, 4))

print(lb.curselection())  # 返回已选中项的下标
print(lb.selection_includes(3))  # 判断此下标是否被选中

win.mainloop()
