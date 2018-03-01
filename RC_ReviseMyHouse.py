#Ruhika Chatterjee
#Python Period 5
#March 23, 2016
#Scale and translate yi_myHouse

import pygame, sys
from pygame.locals import *

# set up the colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 20)
GREEN = (76, 153, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

# set up pygame
pygame.init()

# set up the window
windowSurface = pygame.display.set_mode((800, 800), 0, 32)
pygame.display.set_caption('My House')

def drawHouse (x, y, scale):
    pygame.draw.rect(windowSurface, RED, (x, y, scale, scale), 0)
    pygame.draw.polygon(windowSurface, GREEN, ((x-10, y), (x+(scale/2), y-(scale/2)), (x+10+scale, y)))
    pygame.draw.rect(windowSurface, BLACK, (x+(scale/5), y+(scale/5), scale/5, scale/5), 0)

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    windowSurface.fill(WHITE)
    pygame.draw.polygon(windowSurface, GREEN, ((0, 800), (800, 800), (800, 620), (0,620)))
    drawHouse (50, 400, 250)
    drawHouse (370, 270, 400)
    pygame.display.update()
