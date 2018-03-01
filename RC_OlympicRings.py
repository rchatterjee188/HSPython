import pygame, sys
from pygame.locals import *

WHITE = (255, 255, 255)
BLUE = (0, 0, 200)
YELLOW = (204, 204, 0)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def initialize ():
    pygame.init()

def setWindow ():
    windowSurface = pygame.display.set_mode((900, 600), 0, 32)
    pygame.display.set_caption('Olympic Rings')
    windowSurface.fill(WHITE)

    pygame.draw.circle(windowSurface, BLUE, (150, 220), 140, 15)
    pygame.draw.circle(windowSurface, BLACK, (450, 220), 140, 15)
    pygame.draw.circle(windowSurface, RED, (750, 220), 140, 15)
    pygame.draw.circle(windowSurface, GREEN, (600, 380), 140, 15)
    pygame.draw.circle(windowSurface, YELLOW, (300, 380), 140, 15)
    

def drawWindow ():
    pygame.display.update()

def gameLoop ():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
def main ():
    initialize ()
    setWindow ()
    drawWindow ()
    gameLoop ()
    
main ()
