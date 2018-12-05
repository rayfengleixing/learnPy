#!/usr/bin/env python
# -*- coding:utf-8 -*- 

import random

s = random.randint(0,101)

while True:
    n = int(input("Input a number between 0～100>> "))

    if n > s:
        print("bigger")
    elif n < s:
        print("smaller")
    else:
        print("Yes it's %s"%s)
        break

