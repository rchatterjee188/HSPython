#Ruhika Chatterjee
#Python Period 5
#May 6, 2016
#Space Invaders

import pygame, sys, random
from pygame.locals import *

WINDOWHEIGHT = 400
WINDOWWIDTH = 400

MOVESPEED = 3
INVADERMOVESPEED = 2

BLACK = (0,0,0)
GREEN = (0,204,0)
WHITE = (255,255,255)
RED = (204,0,0)

def drawText (windowSurface, text, location, textcolor, backgroundcolor):
    fontObj = pygame.font.SysFont(None, 20)
    
    tSurfObj = fontObj.render(text, True, textcolor, backgroundcolor)
    
    tRectObj = tSurfObj.get_rect()
    
    tRectObj.center = location

    windowSurface.blit(tSurfObj, tRectObj)

def moveDefender ():
    global defender, moveRight, moveLeft
    
    if moveRight and defender.right < WINDOWWIDTH:
        defender.right += MOVESPEED
    if moveLeft and defender.left > 0:
        defender.left -= MOVESPEED

def moveInvaders():
    global invaders, invaderDirection
    
    for column in invaders:
        for invader in column:
            if invaderDirection == 'right':
                invader.right += invaderSpeed
            if invaderDirection == 'left':
                invader.left -= invaderSpeed

    if invaderDirection == 'right' and invaders[-1][0].right > WINDOWWIDTH:
        invaderDirection = 'left'
        for column in invaders:
            for invader in column:
                invader.top += invaderSpeed
    if invaderDirection == 'left' and invaders[0][0].left < 0:
        invaderDirection = 'right'
        for column in invaders:
            for invader in column:
                invader.top += invaderSpeed

def addBullets ():
    global bullets, addBullet, defender, invaderBullet, invaders
    
    if addBullet:
        bullets['player'].append (pygame.Rect(defender.center[0], defender.center[1], 3,7))
        addBullet = False

    invaderBullet += random.randint (0,5)
    if invaderBullet >= 75:
        invaderShootCoordinate = random.choice(invaders)[-1].center
        bullets['invader'].append (pygame.Rect(invaderShootCoordinate[0], invaderShootCoordinate[1], 3,7))
        invaderBullet = 0

def moveBullets ():
    global bullets
    
    if len (bullets['player']) > 0:
        for bullet in bullets['player']:
            bullet.top -= MOVESPEED
        for bullet in bullets['player'][:]:
            if bullet.top < 0:
                bullets['player'].remove(bullet)
    
    if len (bullets['invader']) > 0:
        for bullet in bullets['invader']:
            bullet.top += MOVESPEED
        for bullet in bullets['invader'][:]:
            if bullet.bottom > WINDOWHEIGHT:
                bullets['invader'].remove(bullet)

def bulletsHit ():
    global bullets, invaders, score, defender, lives, houses
    
    for bullet in bullets['player'][:]:
        for column in range(len(invaders)):
            for i in invaders[column][:]:
                if bullet.colliderect (i):
                    bullets['player'].remove(bullet)
                    invaders[column].remove(i)
                    score += 20

    for bullet in bullets['invader'][:]:
        if bullet.colliderect (defender):
            bullets['invader'].remove(bullet)
            lives -= 1

    for bullet in bullets['invader'][:]:
        for house in houses:
            if bullet.colliderect(house):
                bullets['invader'].remove(bullet)
                house.top += 3
                house.height -= 3

    for bullet in bullets['player'][:]:
        for house in houses:
            if bullet.colliderect(house):
                bullets['player'].remove(bullet)
                house.height -= 3

def drawRects ():
    global windowSurface, bullets, invaders, houses
    
    for bullet in bullets['player']:
        pygame.draw.rect (windowSurface, RED, bullet)
    for bullet in bullets['invader']:
        pygame.draw.rect (windowSurface, RED, bullet)

    pygame.draw.rect (windowSurface, GREEN, defender)

    for column in invaders:
        for invader in column:
            pygame.draw.rect (windowSurface, WHITE, invader)

    for house in houses:
        pygame.draw.rect(windowSurface, RED, house)

def main():
    global windowSurface, defender, moveRight, moveLeft, invaders, invaderDirection, houses, bullets, addBullet, invaderBullet, lives, score, invaderSpeed
    
    pygame.init()
    mainClock = pygame.time.Clock()

    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption('Space Invaders')
    
    gameOver = False
    level = 1
    score = 0

    invaderSpeed = 2
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    gameOver = False
                    level += 1
                    invaderSpeed += 2

        if gameOver == False:
            defender = pygame.Rect(20, WINDOWHEIGHT - 30, 25, 15)
            moveRight = False
            moveLeft = False
            
            invaders = [[],[],[],[],[],[],[],[]]
            for column in range(len(invaders)):
                for i in range(4):
                    invaders[column].append (pygame.Rect(10+(column*20), 10 + (i*20), 10, 10))
            invaderDirection = 'right'
            
            houses = []
            for x in range (5):
                houses.append(pygame.Rect(41 + (71*x), 340, 30, 20))
            
            bullets = {'player':[ ], 'invader':[ ]}
            addBullet = False
            invaderBullet = 0
            
            lives = 3
        
        while not gameOver:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_LEFT or event.key == ord('a'):
                        moveRight = False
                        moveLeft = True
                    if event.key == K_RIGHT or event.key == ord('d'):
                        moveRight = True
                        moveLeft = False
                    if event.key == K_SPACE:
                        addBullet = True
                if event.type == KEYUP:
                    if event.key == K_RIGHT or event.key == K_LEFT or event.key == ord('a') or event.key == ord('d'):
                        moveRight = False
                        moveLeft = False
            
            moveDefender ()
            moveInvaders()
            
            addBullets ()
            moveBullets ()
            bulletsHit ()
            
            for column in invaders[:]:
                if len(column) == 0:
                    invaders.remove(column)

            for house in houses[:]:
                if house.height <= 0:
                    houses.remove(house)

            if len(invaders) == 0 or lives == 0:
                gameOver = True
            for column in invaders[:]:
                for house in houses[:]:
                    if column[-1].bottom >= house.top:
                        gameOver = True
            
            windowSurface.fill (BLACK)
            
            drawRects ()

            drawText (windowSurface, 'Lives: ' + str(lives), (30, WINDOWHEIGHT-10), RED, BLACK)
            drawText (windowSurface, 'Score: ' + str(score), (100, WINDOWHEIGHT-10), RED, BLACK)
            
            pygame.display.update()
            mainClock.tick(60)
        
        windowSurface.fill (BLACK)
        drawText (windowSurface, 'Game Over', (WINDOWWIDTH/2, WINDOWHEIGHT/2), RED, BLACK)
        drawText (windowSurface, 'Lives: ' + str(lives), (30, WINDOWHEIGHT-10), RED, BLACK)
        drawText (windowSurface, 'Score: ' + str(score), (100, WINDOWHEIGHT-10), RED, BLACK)
        drawText (windowSurface, 'Click the Space Bar to Play Again', (110, 15), RED, BLACK)

        pygame.display.update()

main()
