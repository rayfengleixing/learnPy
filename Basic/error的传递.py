#!/usr/bin/python3
#-*- coding:utf-8 -*-

def test1():
    print("-------test1-1--------")
    print(num)
    print("-------test1-2--------")

def test2():
    print("-------test2-1--------")
    test1()
    print("-------test2-2--------")

def test3():
    try:
        print("-------test3-1--------")
        test2()
        print("-------test3-2--------")
    except Exception as e:
        print("程序的异常是%s"%e)

test3()
print("----------华丽的分割线-------------")
test2()
