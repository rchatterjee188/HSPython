import pygame, sys
from pygame.locals import *

# set up pygame
pygame.init()

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 20)
GREEN = (76, 153, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# set up the window
windowSurface = pygame.display.set_mode((800, 800), 0, 32)
pygame.display.set_caption('My House')
windowSurface.fill(WHITE)
pygame.draw.polygon(windowSurface, GREEN, ((0, 800), (800, 800), (800, 620), (0,620)))
pygame.draw.polygon(windowSurface, RED, ((50, 620), (270, 620), (270,400), (50, 400)))
pygame.draw.polygon(windowSurface, GREEN, ((40, 400), (280, 400), (160,350)))
pygame.draw.polygon(windowSurface, BLACK, ((160,470), (160,510), (120,510), (120,470)))
pygame.draw.circle(windowSurface, YELLOW, (700, 100), 75, 0)

# draw the window onto the screen
pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

