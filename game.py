import pygame
from pygame.locals import *

gameOver = False

pygame.init()

displaySurf = pygame.display.set_mode((300, 300))

# game loop goes here

while not gameOver:
    # play one step of the game, and test for game over

    # (for now, there is no such test, so this is an endless loop)

    # at the end of each loop, update the display
    pygame.display.update()

pygame.quit()
