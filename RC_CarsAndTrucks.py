#Ruhika Chatterjee
#Python Period 5
#March 23, 2016
#Draw a series of cars and trucks

import pygame, sys, random
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

COLORS = (RED, GREEN, BLUE)

def drawCar (windowSurface,x, y, scale, color):
    pygame.draw.rect(windowSurface, color, (x, y, scale, int(scale/2)), 0)
    pygame.draw.polygon (windowSurface, color, ((int(x+(1/6*scale)), y), (int(x+(1/3*scale)), int(y-(1/3*scale))), (int(x+(2/3*scale)), int(y-(1/3*scale))), (int(x+(5/6*scale)) , y)), 0)
    pygame.draw.circle (windowSurface, BLACK, (int(x+(2/3*scale)),int(y+(1/2*scale))), int(scale/10), 0)
    pygame.draw.circle (windowSurface, BLACK, (int(x+(1/3*scale)),int(y+(1/2*scale))), int(scale/10), 0)
    
def drawTruck(windowSurface,x, y, scale, color):
    pygame.draw.rect(windowSurface, color, (x, y, scale, int(scale/2)), 0)
    pygame.draw.rect(windowSurface, color, (x, int(y-(scale/4)), int(scale*(2/3)), int(scale/2)), 0)
    pygame.draw.circle (windowSurface, BLACK, (int(x+(2/3*scale)),int(y+(1/2*scale))), int(scale/10), 0)
    pygame.draw.circle (windowSurface, BLACK, (int(x+(1/3*scale)),int(y+(1/2*scale))), int(scale/10), 0)

def main():
    pygame.init()
    
    windowSurface = pygame.display.set_mode((1000, 800), 0, 32)
    pygame.display.set_caption('Cars and Trucks')
    
    windowSurface.fill(WHITE)
    
    for x in range (random.randint(5,20)):
        drawCar (windowSurface, random.randint(0, 1000), random.randint(0, 800), random.randint(10, 200), random.choice(COLORS))
        drawTruck (windowSurface, random.randint(0, 1000), random.randint(0, 800), random.randint(10, 200), random.choice(COLORS))
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

main()
