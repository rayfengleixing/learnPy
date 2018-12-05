#!/usr/bin/env python
# -*- coding:utf-8 -*-

# @Author  : Ray
# @File    : test.py
# @Time    : 2018/11/1  18:45
# @Software: PyCharm
# @DESC    :

s = ''


def a(s):
    s = 'sssssssssssss'
    print(s)


def one():
    global s
    s = 'one'
    a(s)
    print(s)


def two():
    global s
    s = 'two'
    a(s)
    print(s)


def show():
    global s
    s = 'show'
    a(s)
    print(s)


a(s)
one()
show()
