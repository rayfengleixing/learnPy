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

    def display(self):
        self.screen.blit(self.img,(self.x, self.y))
    
    def moveLeft(self):
        self.x -= 10

    def moveRight(self):
        self.x += 10

    def moveUp(self):
        self.y -= 10

    def moveDown(self):
        self.y += 10


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


def main():
    screen = pygame.display.set_mode((480, 652), 0, 32)
    background = pygame.image.load("./feiji/background.png")
    hero = Plane(screen)

    while True:
        screen.blit(background,(0,0))
        hero.display()
        pygame.display.update()

        keyControl(hero)

        time.sleep(0.05)




if __name__ == "__main__":
    main()
