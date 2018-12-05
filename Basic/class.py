#!/usr/bin/python3
# -*- coding:utf-8 -*-


class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "%s的年龄是：%d" % (self.name, self.age)

    def eat(self):
        print("%s is eating!" % self.name)

    def run(self):
        print("%s is running!" % self.name)


mm = Cat('咪咪', 6)
xh = Cat('小花', 4)
print(mm)
mm.eat()
mm.run()
print(xh)
xh.eat()
xh.run()
