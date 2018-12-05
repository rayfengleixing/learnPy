#!/usr/bin/python3
#-*- coding:utf-8 -*-

class Test(object):
    def __init__(self, switch):
        self.switch = switch

    def calc(self, a, b):
        try:
            return a/b
        except Exception as e:
            if self.switch:
                print("the error is:")
                print(e)
            else:
                raise#raise后面如果不跟自定义异常的话，原本程序异常会是什么样，就是什么样

a = Test(True)
a.calc(8, 0)

print("-------------------------")
a.switch = False
a.calc(8, 0)
