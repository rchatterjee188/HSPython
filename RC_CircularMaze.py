#Ruhika Chatterjee
#Python Period 5
#April 8, 2016
#Draw a circle maze

import pygame, sys, math
from pygame.locals import *

WHITE = (255, 255, 255)
MINT = (204, 255, 229)
BLACK = (0, 0, 0)

def drawText (windowSurface, text, location):
    fontObj = pygame.font.Font('freesansbold.ttf', 10)
    
    tSurfObj = fontObj.render(text, True, BLACK, MINT)
    
    tRectObj = tSurfObj.get_rect()
    
    tRectObj.center = location

    windowSurface.blit(tSurfObj, tRectObj)

def drawLines (windowSurface):
    pygame.draw.circle (windowSurface, BLACK, (200,200), 200, 5)
    
    pygame.draw.arc (windowSurface, BLACK, (30,30,340,340), math.radians(90), math.radians(320), 5)
    pygame.draw.arc (windowSurface, BLACK, (30,30,340,340), math.radians(50), math.radians(75), 5)
    pygame.draw.arc (windowSurface, BLACK, (30,30,340,340), math.radians(0), math.radians(40), 5)
    pygame.draw.arc (windowSurface, BLACK, (70,70,260,260), math.radians(0), math.radians(160), 5)
    pygame.draw.arc (windowSurface, BLACK, (70,70,260,260), math.radians(250), math.radians(330), 5)
    pygame.draw.arc (windowSurface, BLACK, (70,70,260,260), math.radians(170), math.radians(230), 5)
    pygame.draw.arc (windowSurface, BLACK, (100,100,200,200), math.radians(250), math.radians(330), 5)
    pygame.draw.arc (windowSurface, BLACK, (120,120,160,160), math.radians(-120), math.radians(180), 5)
    pygame.draw.arc (windowSurface, BLACK, (150,150,100,100), math.radians(-270), math.radians(30), 5)
    
    pygame.draw.line (windowSurface, BLACK, (10, 250), (38,239), 5)
    pygame.draw.line (windowSurface, BLACK, (145, 145), (165,165), 5)
    pygame.draw.line (windowSurface, BLACK, (327, 200), (400,200), 4)
    pygame.draw.line (windowSurface, BLACK, (200, 70), (200,123), 4)
    pygame.draw.line (windowSurface, BLACK, (308, 268), (280,254), 5)
    pygame.draw.line (windowSurface, BLACK, (305, 70), (325,45), 5)

def main():
    pygame.init()
    
    windowSurface = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('Circle Maze')
    
    while True:
        windowSurface.fill(MINT)

        drawText (windowSurface, 'START', (200, 20))
        drawText (windowSurface, 'END', (200, 220))
        
        drawLines (windowSurface)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()

main()

