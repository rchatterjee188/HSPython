import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()

# set up the colors
BLACK = (0, 0, 0)
WHITE = (237, 173, 100)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# set up the window
windowSurface = pygame.display.set_mode((1200, 900), 0, 32)
pygame.display.set_caption('Hello world!')
windowSurface.fill(WHITE)
pygame.draw.polygon(windowSurface, BLUE, ((423, 700), (208, 700), (15, 100)))
pygame.draw.polygon(windowSurface, BLUE, ((453, 700), (238, 100), (45, 100)))
#pygame.draw.line(windowSurface, RED, ((453, 200), (238, 100)), 10)
pygame.draw.circle(windowSurface, GREEN, (100, 1000), 32, 5)
pygame.draw.ellipse(windowSurface, BLACK, (1000, 500, 200, 10), 0)
pygame.draw.rect(windowSurface, (255, 255, 255), ((25, 27, 28, 32)))

# draw the window onto the screen
pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
