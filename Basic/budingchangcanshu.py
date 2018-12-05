#!/usr/bin/python3
# coding=utf-8

def test(a, b, c=33, *args, **kwargs):
    """不定长参数的定义，*args将已定义外的参数全放进一个元组(tuple)里面，
    **kwargs将下面的键值对存进字典(dict)里面"""
    print(a)
    print(b)
    print(c)
    print(args)
    print(kwargs)

test(11,22,44,55,name='wmn', age=26)
