import pygame
from pygame.locals import *

BLACK = pygame.color.Color(0,0,0)
RED = pygame.color.Color(255,0,0)
WHITE = pygame.color.Color(255,255,255)

gameOver = False

pygame.init()

displaySurf = pygame.display.set_mode((300, 300))
displaySurf.fill(WHITE)
pygame.draw.circle(displaySurf, RED, (200,50), 30)

# game loop goes here

while not gameOver:
    # play one step of the game, and test for game over

    # get events
    for event in pygame.event.get():
        # check what kind of event we got; first check for quit
        if event.type == QUIT:
            gameOver = True # if user quits, game is over

    # at the end of each loop, update the display
    pygame.display.update()

pygame.quit()
