#!/usr/bin/env python
# -*- coding:utf-8 -*-


import random

while True:
    
    print("\n\n1 = 石头, 2 = 剪刀, 3 = 布")
    
    s = random.randint(1, 3)
    n = int(input("Please input your num>> "))
    l = ['石头', '剪刀', '布']
    
    if n not in range(1, 4):
        print(">>       wrong num")
        break
    elif n == 1 and s == 2 or n == 2 and s == 3 or n == 3 and s == 1:
        print(">>       You Win!")
        print(">>       You are %s, the computer is %s"%(l[n-1],l[s-1]))
    elif n == 2 and s == 1 or n == 3 and s == 2 or n == 1 and s == 3:
        print(">>       You Lose!")
        print(">>       You are %s, the computer is %s"%(l[n-1],l[s-1]))
    else:
        print(">>       You == Computer")
        print(">>       You are %s, the computer is %s"%(l[n-1],l[s-1]))
