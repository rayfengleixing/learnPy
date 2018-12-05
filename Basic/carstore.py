#!/usr/bin/python3
#-*- coding:utf-8 -*-

class CarStore(object):

    def __init__(self):
        self.factory = Factory()

    def order(self, carType):
        return self.factory.selectCarType(carType)


class Factory(object):
    def selectCarType(self, carType):
        if carType == 'suntana':
            return Suntana()
        elif carType == 'qrqq':
            return  Qrqq()


class Car(object):
    # def __init__(self,name):
        # self.name = name
    def move(self):
        print("car is moving")
    def stop(self):
        print("cat is stopping")

class Suntana(Car):
    pass
class Qrqq(Car):
    pass

carStore = CarStore()
car = carStore.order("suntana")
car.move()
car.stop()
