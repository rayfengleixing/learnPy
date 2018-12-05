#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : 仿写class-很懵.py
# @Time    : 2018/10/29  22:08
# @Software: PyCharm
# @DESC    :

import tkinter as tk


class Window(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master.title("class test")
        self.master.geometry("200x100+400+200")
        self.master.resizable(0, 0)
        self.pack()
        self.btn_hi = None
        self.btn_quit = None
        self.label = None
        self.create_widget()

    def create_widget(self):
        self.btn_hi = tk.Button(self)
        self.btn_hi['text'] = "I want..."
        self.btn_hi['command'] = self.say_hi
        self.btn_hi.pack()

        self.btn_quit = tk.Button(self)
        self.btn_quit['text'] = "QUIT"
        self.btn_quit['command'] = self.quit()

        self.label = tk.Label(self)
        self.label['text'] = 'What ?'
        self.label['font'] = ('楷体', 20)
        self.label.pack()

    def say_hi(self):
        self.label['text'] = "You"
        self.btn_hi.configure(text='Fuck')
        self.btn_hi.configure(state='disabled')


root = tk.Tk()
win = Window(master=root)
win.mainloop()
