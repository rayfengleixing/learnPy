#!/usr/bin/python3
# coding=utf-8


def getNums(num):
    if num > 1:
        return num * getNums(num - 1)
    else:
        return num


print(getNums(5))
