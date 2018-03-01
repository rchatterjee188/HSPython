import pygame, sys
from pygame.locals import *

# set up the colors
WHITE = (255, 255, 255)
YELLOW = (255, 255, 153)
ORANGE = (255, 139, 0)
BROWN = (155, 100, 0)
PURPLE = (51, 0, 51)

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((900, 900), 0, 32)
pygame.display.set_caption('Bullseye!')
windowSurface.fill(WHITE)

pygame.draw.circle(windowSurface, YELLOW, (450, 450), 280, 0)
pygame.draw.circle(windowSurface, ORANGE, (450, 450), 210, 0)
pygame.draw.circle(windowSurface, BROWN, (450, 450), 140, 0)
pygame.draw.circle(windowSurface, PURPLE, (450, 450), 70, 0)

# draw the window onto the screen
pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
