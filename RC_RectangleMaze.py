#Ruhika Chatterjee
#Python Period 5
#April 4, 2016
#Draw a rectangle maze

import pygame, sys
from pygame.locals import *
import time

WHITE = (255, 255, 255)
MINT = (204, 255, 229)
BLACK = (0, 0, 0)
RED = (246, 45, 45)

def drawStartEnd ():
    fontObj = pygame.font.Font('freesansbold.ttf', 10)

    tSurfObj1 = fontObj.render('START', True, BLACK, MINT)
    tSurfObj2 = fontObj.render('END', True, BLACK, MINT)

    tRectObj1 = tSurfObj1.get_rect()
    tRectObj2 = tSurfObj2.get_rect()

    tRectObj1.center = (50, 20)
    tRectObj2.center = (350, 320)

    return tSurfObj1, tSurfObj2, tRectObj1, tRectObj2

def drawLines (windowSurface):
    pygame.draw.lines (windowSurface, BLACK, True, ((0,0), (400,0), (400,400), (0,400)), 8)
    pygame.draw.line (windowSurface, BLACK, (100, 0), (100, 325), 5)
    pygame.draw.line (windowSurface, BLACK, (200, 400), (200, 200), 5)
    pygame.draw.line (windowSurface, BLACK, (200, 200), (350, 200), 5)
    pygame.draw.line (windowSurface, BLACK, (150, 200), (300, 200), 5)
    pygame.draw.line (windowSurface, BLACK, (270, 200), (270, 100), 5)
    pygame.draw.line (windowSurface, BLACK, (400, 300), (300, 300), 5)
    pygame.draw.line (windowSurface, BLACK, (200, 0), (200, 125), 5)
    pygame.draw.line (windowSurface, BLACK, (300, 350), (300, 250), 5)
    pygame.draw.line (windowSurface, BLACK, (400, 50), (300, 50), 5)
    pygame.draw.line (windowSurface, BLACK, (75, 325), (125, 325), 5)

def setPixelArray (windowSurface):
    pixArray = pygame.PixelArray (windowSurface)
    for a in range (2,98):
        for b in range (2, 40):
            pixArray[a][b] = RED
            
    for x in range (303, 398):
        for y in range (303, 340):
            pixArray[x][y] = RED
    
    return pixArray

def main():
    pygame.init()

    windowSurface = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Rectange Maze')

    textSurfObj1, textSurfObj2, textRectObj1, textRectObj2 = drawStartEnd ()
    
    while True:
        windowSurface.fill(MINT)
        
        pixArray = setPixelArray (windowSurface)
        
        del pixArray
        
        windowSurface.blit(textSurfObj1, textRectObj1)
        windowSurface.blit(textSurfObj2, textRectObj2)
        
        drawLines (windowSurface)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        
        
        

main()

