#!/usr/bin/env python
# -*- coding:utf-8 -*-

fileName = input("请输入你要复制的文件名的完整路径：")

f = open(fileName, 'r', encoding='utf-8')

idx = fileName.find(".")
print(idx)
print(fileName[:idx])

fileNameNew = fileName[:idx] + '_复件' + fileName[idx:]

f2 = open(fileNameNew, 'w', encoding="utf-8")

# content = f.read()
# f2.write(content)
while True:
    content = f.read()
    if len(content) == 0:
        break
    f2.write(content)

f.close()
f2.close()
