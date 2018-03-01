#Ruhika Chatterjee
#Python Period 5
#April 29, 2016
#One player pong game

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
WHITE = (255,255,255)

def drawText (windowSurface, text, location, textcolor, backgroundcolor):
    fontObj = pygame.font.SysFont(None, 20)
    
    tSurfObj = fontObj.render(text, True, textcolor, backgroundcolor)
    
    tRectObj = tSurfObj.get_rect()
    
    tRectObj.center = location

    windowSurface.blit(tSurfObj, tRectObj)

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

def main():
    pygame.init()

    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption('Pong')

    gamePlaying = True
    
    bouncer = {'rect':pygame.Rect(20, random.randrange(0,WINDOWHEIGHT), 30, 20), 'color':RED, 'dir':DOWNRIGHT}
    
    player = pygame.Rect(WINDOWWIDTH - 30, WINDOWHEIGHT/2, 10, 60)
    moveDown = False
    moveUp = False

    score = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP or event.key == ord('w'):
                    moveUp = True
                    moveDown = False
                if event.key == K_DOWN or event.key == ord('s'):
                    moveUp = False
                    moveDown = True
            if event.type == KEYUP:
                moveUp = False
                moveDown = False

        if gamePlaying:
            moveBlock (bouncer)
            
            if moveDown and player.bottom < WINDOWHEIGHT:
                player.top += MOVESPEED
            if moveUp and player.top > 0:
                player.top -= MOVESPEED

            blockScreenBounce (bouncer)
            
            if player.colliderect(bouncer['rect']):
                if bouncer['dir'] == UPRIGHT:
                    bouncer['dir'] = UPLEFT
                if bouncer['dir'] == DOWNRIGHT:
                    bouncer['dir'] = DOWNLEFT
                score += 1
            
            if bouncer['rect'].right > WINDOWWIDTH:
                gamePlaying = False

        windowSurface.fill(MINT)
        
        drawText (windowSurface, 'Score: '+str(score) , (30,20), BLACK, MINT)
        if not gamePlaying:
            drawText (windowSurface, 'GAME OVER', (WINDOWWIDTH/2, WINDOWHEIGHT/2), BLACK, MINT)
        
        pygame.draw.rect(windowSurface, bouncer['color'], bouncer['rect'])
        pygame.draw.rect(windowSurface, BLACK, player)
        
        pygame.display.update()
        time.sleep(0.03)

main()
