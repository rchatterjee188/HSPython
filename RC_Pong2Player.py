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

MOVESPEED = 3

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

def main():
    pygame.init()

    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption('Pong')

    gamePlaying = True
    
    bouncer = {'rect':pygame.Rect(WINDOWWIDTH/2, random.randrange(0,WINDOWHEIGHT), 20, 20), 'color':RED, 'dir': DOWNLEFT}
    
    player1 = pygame.Rect(30, WINDOWHEIGHT/2, 10, 60)
    move1Down = False
    move1Up = False

    player2 = pygame.Rect(WINDOWWIDTH - 30, WINDOWHEIGHT/2, 10, 60)
    move2Down = False
    move2Up = False

    score1 = 0
    score2 = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    move2Up = True
                    move2Down = False
                if event.key == ord('w'):
                    move1Up = True
                    move1Down = False
                if event.key == K_DOWN:
                    move2Up = False
                    move2Down = True
                if event.key == ord('s'):
                    move1Up = False
                    move1Down = True
            if event.type == KEYUP:
                if event.key == K_UP or event.key == K_DOWN:
                    move2Up = False
                    move2Down = False
                if event.key == ord('w') or event.key == ord('s'):
                    move1Up = False
                    move1Down = False
        
        if gamePlaying:
            moveBlock (bouncer)
            
            if move1Down and player1.bottom < WINDOWHEIGHT:
                player1.top += MOVESPEED
            if move1Up and player1.top > 0:
                player1.top -= MOVESPEED
            if move2Down and player2.bottom < WINDOWHEIGHT:
                player2.top += MOVESPEED
            if move2Up and player2.top > 0:
                player2.top -= MOVESPEED

            blockScreenBounce (bouncer)
            
            if player1.colliderect(bouncer['rect']):
                if bouncer['dir'] == UPLEFT:
                    bouncer['dir'] = UPRIGHT
                if bouncer['dir'] == DOWNLEFT:
                    bouncer['dir'] = DOWNRIGHT
                score1 += 1
            if player2.colliderect(bouncer['rect']):
                if bouncer['dir'] == UPRIGHT:
                    bouncer['dir'] = UPLEFT
                if bouncer['dir'] == DOWNRIGHT:
                    bouncer['dir'] = DOWNLEFT
                score2 += 1
            
            if bouncer['rect'].right > WINDOWWIDTH:
                score1 += 1
                bouncer = {'rect':pygame.Rect(WINDOWWIDTH/2, random.randrange(0,WINDOWHEIGHT), 20, 20), 'color':RED, 'dir': DOWNLEFT}
            if bouncer['rect'].left < 0:
                score2 += 1
                bouncer = {'rect':pygame.Rect(WINDOWWIDTH/2, random.randrange(0,WINDOWHEIGHT), 20, 20), 'color':RED, 'dir': DOWNRIGHT}

            if score1 >= 10 or score2 >= 10:
                gamePlaying = False

        windowSurface.fill(MINT)
        
        drawText (windowSurface, 'Player 1 Score: '+str(score1) , (WINDOWWIDTH/2,20), BLACK, MINT)
        drawText (windowSurface, 'Player 2 Score: '+str(score2) , (WINDOWWIDTH/2,50), BLACK, MINT)
        
        if not gamePlaying:
            if score1 > score2: winner = '1'
            else:   winner = '2'
            drawText (windowSurface, 'GAME OVER', (WINDOWWIDTH/2, WINDOWHEIGHT/2), BLACK, MINT)
            drawText (windowSurface, 'Player ' + winner + ' won!', (WINDOWWIDTH/2, WINDOWHEIGHT/2+30), BLACK, MINT)
        
        pygame.draw.rect(windowSurface, bouncer['color'], bouncer['rect'])
        pygame.draw.rect(windowSurface, BLACK, player1)
        pygame.draw.rect(windowSurface, BLACK, player2)
        
        pygame.display.update()
        time.sleep(0.03)

main()
