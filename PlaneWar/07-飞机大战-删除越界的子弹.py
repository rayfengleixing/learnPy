#!/usr/bin/python3
#-*- coding:utf-8 -*-

import pygame
from pygame.locals import *
import time


class Plane(object):
    def __init__(self, screen):
        self.x = 200
        self.y = 530
        self.screen = screen
        self.img = pygame.image.load("./feiji/hero1.png")
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.img,(self.x, self.y))

        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():#判断子弹是否越界
                self.bullet_list.remove(bullet)#谁越界就删除谁
    
    def moveLeft(self):
        self.x -= 10

    def moveRight(self):
        self.x += 10

    def moveUp(self):
        self.y -= 10

    def moveDown(self):
        self.y += 10

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))

class Enemy(object):
    """敌机类"""
    def __init__(self, screen):
        self.x = 200
        self.y = 0
        self.screen = screen
        self.img = pygame.image.load("./feiji/enemy0.png")
        self.bullet_list = []
        self.direction = "right"

    def display(self):
        self.screen.blit(self.img,(self.x, self.y))
        self.move()
        # for bullet in self.bullet_list:
            # bullet.display()
            # bullet.move()
    
    def move(self):
        self.y += 5
        if self.direction == "left":
            self.x -= 10
        elif self.direction == "right":
            self.x += 10

        if self.x >= 400:
            self.direction = "left"
        elif self.x <= 0:
            self.direction = "right"

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))


class Bullet(object):
    def __init__(self, screen, x, y):
        self.x = x + 40
        self.y = y - 10
        self.screen = screen
        self.img = pygame.image.load("./feiji/bullet.png")

    def display(self):
        self.screen.blit(self.img, (self.x, self.y))

    def move(self):
        self.y -= 10

    def judge(self):
        if self.y <= 0:
            return True
        else:
            return False

def keyControl(hero):

    for event in pygame.event.get():
        #判断是否点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
        elif event.type == KEYDOWN:
            #判断是否按下了a或者left键
            if event.key == K_a or event.key == K_LEFT:
                hero.moveLeft()
                print("left")
            #判断是否按下了d或者right键
            elif event.key == K_d or event.key == K_RIGHT:
                hero.moveRight()
                print("right")
            #w or up  同理
            elif event.key == K_w or event.key == K_UP:
                hero.moveUp()
                print("up")
            #s or down 同理
            elif event.key == K_s or event.key == K_DOWN:
                hero.moveDown()
                print("down")
            
            #判断是否点击了空格键
            elif event.key == K_SPACE:
                print("space")
                hero.fire()


def main():
    screen = pygame.display.set_mode((480, 652), 0, 32)
    background = pygame.image.load("./feiji/background.png")
    hero = Plane(screen)
    enemy = Enemy(screen)

    while True:
        screen.blit(background,(0,0))
        hero.display()
        enemy.display()
        pygame.display.update()

        keyControl(hero)

        time.sleep(0.05)




if __name__ == "__main__":
    main()
