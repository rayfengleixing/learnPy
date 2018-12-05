#!/usr/bin/python3
#-*- coding:utf-8 -*-

import pygame
from pygame.locals import *
import time

def main():
    screen = pygame.display.set_mode((480, 652), 0, 32)
    background = pygame.image.load("./feiji/background.png")
    hero = pygame.image.load("./feiji/hero1.png")

    x = 200
    y = 530
    while True:
        screen.blit(background,(0,0))
        screen.blit(hero,(x, y))
        pygame.display.update()

        for event in pygame.event.get():
            #判断是否点击了退出按钮
            if event.type == QUIT:
                print("exit")
                exit()
            elif event.type == KEYDOWN:
                #判断是否按下了a或者left键
                if event.key == K_a or event.key == K_LEFT:
                    x -= 15
                    print("left")
                #判断是否按下了d或者right键
                elif event.key == K_d or event.key == K_RIGHT:
                    x += 15
                    print("right")
                #w or up  同理
                elif event.key == K_w or event.key == K_UP:
                    y -= 15
                    print("up")
                #s or down 同理
                elif event.key == K_s or event.key == K_DOWN:
                    y += 15
                    print("down")
                
                #判断是否点击了空格键
                elif event.key == K_SPACE:
                    print("space")

        time.sleep(0.05)




if __name__ == "__main__":
    main()
