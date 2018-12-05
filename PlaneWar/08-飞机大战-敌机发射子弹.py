#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pygame
from pygame import *
from pygame.locals import *
import time
import random


class Base(object):

    def __init__(self, screen, x, y, imgUrl):
        self.x = x
        self.y = y
        self.screen = screen
        self.img = pygame.image.load(imgUrl)

    def display(self):
        self.screen.blit(self.img, (self.x, self.y))


class Plane(Base):

    def __init__(self, screen, x, y, imgUrl):
        super().__init__(screen, x, y, imgUrl)
        self.bullet_list = []

    def display(self):
        self.screen.blit(self.img, (self.x, self.y))
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():  # 判断子弹是否越界
                self.bullet_list.remove(bullet)  # 谁越界就删除谁


class Bullets(Base):
    pass


class Hero(Plane):
    def __init__(self, screen):
        super().__init__(screen, 200, 530, "./feiji/hero1.png")

    def moveLeft(self):
        self.x -= 15

    def moveRight(self):
        self.x += 15

    def moveUp(self):
        self.y -= 15

    def moveDown(self):
        self.y += 15

    def fire(self):
        self.bullet_list.append(Bullet(self.screen, self.x, self.y))


class Enemy(Plane):
    """敌机类"""

    def __init__(self, screen):
        super().__init__(screen, 200, 0, "./feiji/enemy0.png")
        self.direction = "right"

    def move(self):
        self.y += 3
        if self.direction == "left":
            self.x -= 10
        elif self.direction == "right":
            self.x += 10

        if self.x >= 400:
            self.direction = "left"
        elif self.x <= 0:
            self.direction = "right"

    def fire(self):
        random_num = random.randint(1, 25)
        if random_num == 10 or random_num == 14:
            self.bullet_list.append(EnemyBullet(self.screen, self.x, self.y))


class Bullet(Bullets):
    def __init__(self, screen, x, y):
        super().__init__(screen, x + 40, y - 10, "./feiji/bullet.png")

    def move(self):
        self.y -= 20

    def judge(self):
        if self.y <= 0:
            return True
        else:
            return False


class EnemyBullet(Bullets):
    def __init__(self, screen, x, y):
        super().__init__(screen, x + 15, y + 30, "./feiji/bullet1.png")

    def move(self):
        self.y += 10

    def judge(self):
        if self.y >= 630:
            return True
        else:
            return False


def keyControl(hero):
    for event in pygame.event.get():
        # 判断是否点击了退出按钮
        if event.type == QUIT:
            exit()
        elif event.type == KEYDOWN:
            # 判断是否按下了a或者left键
            if event.key == K_a or event.key == K_LEFT:
                hero.moveLeft()
            # 判断是否按下了d或者right键
            elif event.key == K_d or event.key == K_RIGHT:
                hero.moveRight()
            # w or up  同理
            elif event.key == K_w or event.key == K_UP:
                hero.moveUp()
            # s or down 同理
            elif event.key == K_s or event.key == K_DOWN:
                hero.moveDown()

            # 判断是否点击了空格键
            elif event.key == K_SPACE:
                hero.fire()


def main():
    screen = pygame.display.set_mode((480, 652), 0, 32)
    background = pygame.image.load("./feiji/background.png")
    hero = Hero(screen)
    enemy = Enemy(screen)

    while True:
        screen.blit(background, (0, 0))
        hero.display()
        enemy.display()
        enemy.move()
        enemy.fire()
        pygame.display.update()

        keyControl(hero)

        time.sleep(0.05)


if __name__ == "__main__":
    main()
