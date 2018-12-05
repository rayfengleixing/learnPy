#!/usr/bin/python3
#-*- coding:utf-8 -*-

try:
    print(8/0)
    # open("xxxx.md")
    # print(foo)
    print("I am in try!\n")
except (NameError, FileNotFoundError):
    print("变量没定义/文件不存在！\n")
except Exception as e:
    print("Exception是所有异常的父类，as e和java中的一样，是打印异常的具体信息。\n")
    print(e,'\n')
else:
    print("没有异常才会执行的功能。\n")
finally:
    print("不管有没有异常都会执行的。\n")

print("--------I'm not in!-----------\n")
