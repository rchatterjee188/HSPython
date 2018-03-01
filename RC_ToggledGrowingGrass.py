import pygame, sys, random
from pygame.locals import *

WINDOWWIDTH = 400
WINDOWHEIGHT = 400

MOVESPEED = 2

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
SKYBLUE = (0,204,204)
YELLOW = (255,255,0)
WHITE = (255, 255, 255)
RAINBLUE = (0,0,255)
GREY = (160,160,160)

NEWDROP = 20
DROPSIZE = 15

SWITHDROP = 120

GRASSHEIGHT = 20

SUNCENTER = 30
SUNRADIUS = 50

CLOUDDIRECTION = 6

def drawClouds (windowSurface, cloudXPos):
    pygame.draw.circle (windowSurface, GREY, (cloudXPos, 40), 30, 0)
    pygame.draw.circle (windowSurface, GREY, (cloudXPos + 50, 40), 45, 0)
    pygame.draw.circle (windowSurface, GREY, (cloudXPos + 100, 40), 30, 0)

def drawText (windowSurface, text, location, textcolor, backgroundcolor):
    fontObj = pygame.font.SysFont(None, 48)
    
    tSurfObj = fontObj.render(text, True, textcolor, backgroundcolor)
    
    tRectObj = tSurfObj.get_rect()
    
    tRectObj.center = location

    windowSurface.blit(tSurfObj, tRectObj)

def moveDrops (windowSurface, rain, sun, grass):
    for raindrop in rain[:]:
        raindrop.top += MOVESPEED
        if grass.colliderect(raindrop):
            grass.top -= MOVESPEED/2
            grass.height += MOVESPEED/2
            rain.remove(raindrop)

    for sundrop in sun[:]:
        (sundrop[0]).top += MOVESPEED
        (sundrop[0]).left += MOVESPEED * sundrop[1]
        if grass.colliderect(sundrop[0]):
            grass.top -= MOVESPEED
            grass.height += MOVESPEED
            sun.remove(sundrop)

def main():
    pygame.init()
    mainClock = pygame.time.Clock()
    
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption('Growing Grass')
    
    cloudXPos = 20
    cloudDirection = 6
    
    dropCounter = 0
    grass = pygame.Rect(0, (WINDOWHEIGHT - GRASSHEIGHT), WINDOWWIDTH, GRASSHEIGHT)
    rain = []
    sun = []
    for i in range(10):
        rain.append(pygame.Rect(random.randint(cloudXPos, cloudXPos+100-DROPSIZE), random.randint(30,30+DROPSIZE), DROPSIZE, DROPSIZE))

    rainSunCounter = 0
    rainOrShine = 'rain'
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        rainSunCounter += 1
        if rainSunCounter >= SWITHDROP:
            rainSunCounter = 0
            if rainOrShine == 'rain':
                rainOrShine = 'sun'
            else:
                rainOrShine = 'rain'
        
        dropCounter += 1
        if dropCounter >= NEWDROP:
            dropCounter = 0
            for i in range (5):
                if rainOrShine == 'rain':
                    rain.append(pygame.Rect(random.randint(cloudXPos, cloudXPos+100-DROPSIZE), random.randint(30,30+DROPSIZE), DROPSIZE, DROPSIZE))
                else:
                    sun.append ([pygame.Rect(random.randint(SUNCENTER-SUNRADIUS, SUNCENTER+SUNRADIUS),random.randint(SUNCENTER-SUNRADIUS, SUNCENTER+SUNRADIUS), DROPSIZE, DROPSIZE),random.choice([0,0.25,0.5,0.75,1,1.5,2,2.5,3,5])])

        if rainOrShine == 'rain':
            if cloudDirection == 6:
                cloudXPos += MOVESPEED
                if cloudXPos + 100 > WINDOWWIDTH:
                    cloudDirection = 4
            
            elif cloudDirection == 4:
                cloudXPos -= MOVESPEED
                if cloudXPos < 0:
                    cloudDirection = 6
        
        windowSurface.fill(SKYBLUE)

        moveDrops (windowSurface, rain, sun, grass)

        if grass.top < 0:
            rain = []
            sun = []
            break

        for i in range(len(sun)):
            pygame.draw.rect(windowSurface, YELLOW, sun[i][0])
        for i in range(len(rain)):
            pygame.draw.rect(windowSurface, RAINBLUE, rain[i])

        if rainOrShine == 'sun':
            pygame.draw.circle(windowSurface, YELLOW, (SUNCENTER, SUNCENTER), SUNRADIUS*2, 0)
        else:
            drawClouds (windowSurface, cloudXPos)
        
        pygame.draw.rect(windowSurface, GREEN, grass)
        
        pygame.display.update()
        mainClock.tick(60)
    
    while True:
        windowSurface.fill(GREEN)
        
        drawText (windowSurface, 'END', (WINDOWWIDTH/2,WINDOWHEIGHT/2), BLACK, GREEN)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()

main ()
