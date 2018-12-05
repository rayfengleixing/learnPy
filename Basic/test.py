#!/usr/bin/python3
#-*- coding:utf-8 -*-

import pymysql

class Foo(object):
    def __init__(self):
        self.ipt = input("Please input something: ")
    def __str__(self):
        return self.ipt
foo = Foo()
print(foo)


