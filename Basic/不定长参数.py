#!/usr/bin/python3
# coding=utf-8
def test(a, b, c=33, *args, **kwargs):
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

test(11,22,44,55,name='wmn', age=26)
