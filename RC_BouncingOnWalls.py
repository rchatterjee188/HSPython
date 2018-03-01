#Ruhika Chatterjee
#Python Period 5
#April 4, 2016
#Have a ball bounce on two walls

import pygame, sys, time, random
from pygame.locals import *

WINDOWWIDTH = 400
WINDOWHEIGHT = 400

DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9

MOVESPEED = 5

MINT = (204, 255, 229)
BLACK = (0, 0, 0)
RED = (246, 45, 45)

LINE1 = {'X' : 225, 'Y1' : 0, 'Y2' : 200}
LINE2 = {'X' : 225, 'Y1' : 280, 'Y2' : WINDOWHEIGHT}

def drawLines (windowSurface):
    pygame.draw.line (windowSurface, BLACK, (LINE1['X'], LINE1['Y1']), (LINE1['X'], LINE1['Y2']), 5)
    pygame.draw.line (windowSurface, BLACK, (LINE2['X'], LINE2['Y1']), (LINE2['X'], LINE2['Y2']), 5)

def drawRect (windowSurface, rect):
    moveBlock (rect)
    blockScreenBounce (rect)
    blockWallBounce (rect, LINE1)
    blockWallBounce (rect, LINE2)
    blockWallTipBounce (rect)
    pygame.draw.rect(windowSurface, rect['color'], rect['rect'])

def moveBlock (rect):
    if rect['dir'] == DOWNLEFT:
        rect['rect'].left -= MOVESPEED
        rect['rect'].top += MOVESPEED
    if rect['dir'] == DOWNRIGHT:
        rect['rect'].left += MOVESPEED
        rect['rect'].top += MOVESPEED
    if rect['dir'] == UPLEFT:
        rect['rect'].left -= MOVESPEED
        rect['rect'].top -= MOVESPEED
    if rect['dir'] == UPRIGHT:
        rect['rect'].left += MOVESPEED
        rect['rect'].top -= MOVESPEED

def blockScreenBounce (rect):
    if rect['rect'].top < 0:
        if rect['dir'] == UPLEFT:
            rect['dir'] = DOWNLEFT
        if rect['dir'] == UPRIGHT:
            rect['dir'] = DOWNRIGHT
    if rect['rect'].bottom > WINDOWHEIGHT:
        if rect['dir'] == DOWNLEFT:
            rect['dir'] = UPLEFT
        if rect['dir'] == DOWNRIGHT:
            rect['dir'] = UPRIGHT
    if rect['rect'].left < 0:
        if rect['dir'] == DOWNLEFT:
            rect['dir'] = DOWNRIGHT
        if rect['dir'] == UPLEFT:
            rect['dir'] = UPRIGHT
    if rect['rect'].right > WINDOWWIDTH:
        if rect['dir'] == DOWNRIGHT:
            rect['dir'] = DOWNLEFT
        if rect['dir'] == UPRIGHT:
            rect['dir'] = UPLEFT

def blockWallTipBounce (rect):
    if rect['rect'].top <= LINE1['Y2'] and rect['rect'].right >= LINE1['X']+3 and rect['rect'].left <= LINE1['X']-3:
        if rect['dir'] == UPLEFT:
            rect['dir'] = DOWNLEFT
        elif rect['dir'] == UPRIGHT:
            rect['dir'] = DOWNRIGHT
        elif rect['dir'] == DOWNLEFT:
            rect['dir'] = UPLEFT
        elif rect['dir'] == DOWNRIGHT:
            rect['dir'] = UPRIGHT
    if rect['rect'].bottom >= LINE2['Y1']+5 and rect['rect'].right >= LINE2['X']+3 and rect['rect'].left <= LINE2['X']-3:
        if rect['dir'] == DOWNLEFT:
            rect['dir'] = UPLEFT
        elif rect['dir'] == DOWNRIGHT:
            rect['dir'] = UPRIGHT
        elif rect['dir'] == UPLEFT:
            rect['dir'] = DOWNLEFT
        elif rect['dir'] == UPRIGHT:
            rect['dir'] = DOWNRIGHT

def blockWallBounce (rect, line):
    if rect['rect'].left == line['X'] and rect['rect'].top >= line['Y1'] and rect['rect'].top <= line['Y2']:
        if rect['dir'] == DOWNLEFT:
            rect['dir'] = DOWNRIGHT
        if rect['dir'] == UPLEFT:
            rect['dir'] = UPRIGHT
    if rect['rect'].right == line['X'] and rect['rect'].top >= line['Y1'] and rect['rect'].top <= line['Y2']:
        if rect['dir'] == DOWNRIGHT:
            rect['dir'] = DOWNLEFT
        if rect['dir'] == UPRIGHT:
            rect['dir'] = UPLEFT

def main():
    pygame.init()

    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption('Animation Maze')

    rect = {'rect':pygame.Rect(20, random.randrange(0,WINDOWHEIGHT), 50, 30), 'color':RED, 'dir':DOWNRIGHT}
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        windowSurface.fill(MINT)
        drawLines (windowSurface)
        
        drawRect (windowSurface, rect)
        
        pygame.display.update()
        time.sleep(0.03)

main()
