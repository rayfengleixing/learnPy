#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pygame
import time


def main():
    screen = pygame.display.set_mode((480, 652), 0, 32)
    background = pygame.image.load("./feiji/background.png")

    while True:
        screen.blit(background, (0, 0))
        pygame.display.update()
        time.sleep(0.05)


if __name__ == "__main__":
    main()
