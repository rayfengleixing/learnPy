#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Base(object):
    def test(self):
        print("--------Base")


class A(Base):
    def test(self):
        print("--------A")


class B(Base):
    def test(self):
        print("--------B")


class C(A, B):
    def test(self):
        print("--------C")


c = C()
c.test()
print(C.__mro__)  # 类名.__mro__  显示关系类
