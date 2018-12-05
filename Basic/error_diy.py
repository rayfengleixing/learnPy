#!/usr/bin/python3
#-*- coding:utf-8 -*-

class TestException(Exception):
    def __init__(self, length, alt):
        self.length = length
        self.alt = alt

def main():
    try:
        inpt = input("please input smth:")
        if len(inpt) < 5:
            raise TestException(len(inpt), 3)
    except TestException as e:
        print("输入内容的最小长度是%d,你输入的内容的长度是%s"%(e.alt, e.length))
    else:
        print("没有异常！")

main()
