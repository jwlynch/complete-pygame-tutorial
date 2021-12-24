#! /usr/bin/env python3

import pygame
from pygame.locals import *
import sys, random

pygame.init()

FPS = 60
FramePerSec  = pygame.time.Clock()

BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(WHITE)

gameOver = False

while not gameOver:
    for event in pygame.event.get():
        if event.type == QUIT:
            gameOver = True
        elif event.type == KEYDOWN:
            if event.key - pygame.K_q:
                gameOver = True
    DISPLAYSURF.fill(WHITE)

    pygame.display.update()
