#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : 登录窗口.py
# @Time    : 2018/10/29  18:14
# @Software: PyCharm
# @DESC    : 代码来自于视频教程 莫烦 Python tkinter

import pickle
import tkinter as tk
import tkinter.messagebox

win = tk.Tk()
win.title("Login")
win.geometry("300x300+350+150")
win.resizable(0, 0)

canvas = tk.Canvas(win, height=200, width=300)
img_file = tk.PhotoImage(file='images/lye.gif')
img = canvas.create_image(0, 0, anchor='nw', image=img_file)
canvas.pack(side='top')

tk.Label(win, text="User Name: ").place(x=30, y=200)
tk.Label(win, text="Password: ").place(x=30, y=230)

var_user_name = tk.StringVar()
var_user_name.set("rayfengleixing")
entry_user_name = tk.Entry(win, textvariable=var_user_name)
entry_user_name.place(x=120, y=200)

var_pwd = tk.StringVar()
entry_pwd = tk.Entry(win, textvariable=var_pwd, show='*')
entry_pwd.place(x=120, y=230)


def user_sign_up():

    def sign_to_ray():
        nn = new_name.get()
        np = new_pwd.get()
        npc = new_pwd_confirm.get()

        with open('users_info.pickle', 'rb') as user_file:
            exist_user_info = pickle.load(user_file)

        if np != npc:
            tk.messagebox.showerror(title='Sorry!', message='The two passwords are different!')
        elif nn in exist_user_info:
            tk.messagebox.showerror(title='Sorry!', message='The user name already exist!')
        else:
            exist_user_info[nn] = np
            with open('users_info.pickle', 'wb') as user_file:
                pickle.dump(exist_user_info, user_file)
            tk.messagebox.showinfo(title='Welcome', message='You have successfully signed up!')
            window_sign_up.destroy()

    window_sign_up = tk.Toplevel(win)
    window_sign_up.geometry('350x200+400+200')
    window_sign_up.title("Please Sing Up!")

    new_name = tk.StringVar()
    new_name.set("rayfengleixing")
    tk.Label(window_sign_up, text='User Name: ').place(x=10, y=10)
    entry_new_name = tk.Entry(window_sign_up, textvariable=new_name)
    entry_new_name.place(x=150, y=10)

    new_pwd = tk.StringVar()
    tk.Label(window_sign_up, text='Password: ').place(x=10, y=50)
    entry_user_pwd = tk.Entry(window_sign_up, textvariable=new_pwd, show='*')
    entry_user_pwd.place(x=150, y=50)

    new_pwd_confirm = tk.StringVar()
    tk.Label(window_sign_up, text="Confirm password: ").place(x=10, y=90)
    entry_user_pwd_confirm = tk.Entry(window_sign_up, textvariable=new_pwd_confirm, show='*')
    entry_user_pwd_confirm.place(x=150, y=90)

    btn_confirm_sign_up = tk.Button(window_sign_up, text="Sign Up", command=sign_to_ray)
    btn_confirm_sign_up.place(x=150, y=130)


btn_sign_up = tk.Button(win, text="Sign Up", command=user_sign_up)
btn_sign_up.place(x=80, y=260)


def user_login():

    user_name = entry_user_name.get()
    user_pwd = entry_pwd.get()

    try:
        with open('users_info.pickle', 'rb') as user_file:
            users_info = pickle.load(user_file)
    except FileNotFoundError:
        with open('users_info.pickle', 'wb') as user_file:
            users_info = {'admin': 'admin'}
            pickle.dump(users_info, user_file)

    if user_name in users_info:
        if user_pwd == users_info[user_name]:
            tk.messagebox.showinfo(title="Welcome", message='How are you! ' + user_name)
        else:
            tk.messagebox.showinfo(message="Error, your password is wrong, try again!")
    else:
        if_sign_up = tk.messagebox.askyesno(title="Welcome",
                                            message='You have not sign up yet. Sign up today?')
        if if_sign_up:
            user_sign_up()


btn_login = tk.Button(win, text="Login", command=user_login)
btn_login.place(x=160, y=260)

win.mainloop()
