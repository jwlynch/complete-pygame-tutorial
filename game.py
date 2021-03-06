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
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image - pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0, 10)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(30, 370), 0)

        def draw(self, surface):
            surface.blit(self.image, self.rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def update(self):
        pressed_keys = pygame.key.get_pressed()

        #if pressed_keys[K_UP]:
            #self.rect.move_ip(0, -5)

        #if pressed_keys[K_DOWN]:
            #self.rect.move_ip(0, 5)

        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)

        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

    def draw(self, surface):
        surface.blit(self.image, self.rect)

P1 = Player()

gameOver = False

while not gameOver:
    for event in pygame.event.get():
        if event.type == QUIT:
            gameOver = True
        elif event.type == KEYDOWN:
            if event.key - pygame.K_q:
                gameOver = True
    P1.update()

    DISPLAYSURF.fill(WHITE)
    P1.draw(DISPLAYSURF)

    pygame.display.update()
    FramePerSec.tick(FPS)
