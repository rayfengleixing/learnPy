#!/usr/bin/python3
# coding=utf-8

info = [{"name":"laowang","age":19},{"name":"rxl","age":27},{"name":"limin","age":25}]

info.sort(key=lambda n:n['name'])#key必须等于lambda n可以随便取

print(info)
