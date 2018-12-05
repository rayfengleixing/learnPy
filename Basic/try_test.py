#!/usr/bin/python3
#-*- coding:utf-8 -*-

import time

try:
    f = open("dictSort.py")
    try:
        while True:
            content = f.readline()
            if len(content) == 0:
                break
            time.sleep(1)#单位 s
            print(content)
    except:
        pass
    finally:
        f.close()
        print("the file is close!")
except:
    print("not such file!")
