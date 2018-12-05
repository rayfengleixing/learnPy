#!/usr/bin/python3
#-*- coding:utf-8 -*-

class Foo(object):
    __instance = None
    __init__flag = False
    def __new__(cls, name):
        if cls.__instance == None:
            cls.__instance = object.__new__(cls)
            return cls.__instance
        else:
            return cls.__instance

    def __init__(self, name):
        if Foo.__init__flag == False:
            self.name = name
            Foo. __init__flag = True

bar = Foo("bar")
baz = Foo("baz")
print(id(bar))
print(id(baz))
print(bar.name)
print(baz.name)

