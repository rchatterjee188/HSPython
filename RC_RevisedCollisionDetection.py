#yi_revisedCollisionDetection.py
#April, 2016
#Python


import pygame, sys, random
from pygame.locals import *

# set up the window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400

# set up direction variables
DOWNLEFT = 1
DOWNRIGHT = 3
UPLEFT = 7
UPRIGHT = 9

MOVESPEED = 4


# set up the colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

NEWFOOD = 40
FOODSIZE = 20

def main():
    # set up pygame
    pygame.init()
    mainClock = pygame.time.Clock()

    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption('Collision Detection')



    # set up the bouncer and food data structures
    foodCounter = 0
    bouncer = {'rect':pygame.Rect(300, 100, 50, 50), 'dir':UPLEFT}
    foods = []
    for i in range(20):
        foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

    # run the game loop
    while True:
        # check for the QUIT event
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        foodCounter += 1
        if foodCounter >= NEWFOOD:
            # add new food
            foodCounter = 0
            foods.append(pygame.Rect(random.randint(0, WINDOWWIDTH - FOODSIZE), random.randint(0, WINDOWHEIGHT - FOODSIZE), FOODSIZE, FOODSIZE))

        # draw the black background onto the surface
        windowSurface.fill(BLACK)

        # move the bouncer data structure
        if bouncer['dir'] == DOWNLEFT:
            bouncer['rect'].left -= MOVESPEED
            bouncer['rect'].top += MOVESPEED
        if bouncer['dir'] == DOWNRIGHT:
            bouncer['rect'].left += MOVESPEED
            bouncer['rect'].top += MOVESPEED
        if bouncer['dir'] == UPLEFT:
            bouncer['rect'].left -= MOVESPEED
            bouncer['rect'].top -= MOVESPEED
        if bouncer['dir'] == UPRIGHT:
            bouncer['rect'].left += MOVESPEED
            bouncer['rect'].top -= MOVESPEED

        # check if the bouncer has move out of the window
        if bouncer['rect'].top < 0:
            # bouncer has moved past the top
            if bouncer['dir'] == UPLEFT:
                bouncer['dir'] = DOWNLEFT
            if bouncer['dir'] == UPRIGHT:
                bouncer['dir'] = DOWNRIGHT
        if bouncer['rect'].bottom > WINDOWHEIGHT:
            # bouncer has moved past the bottom
            if bouncer['dir'] == DOWNLEFT:
                bouncer['dir'] = UPLEFT
            if bouncer['dir'] == DOWNRIGHT:
                bouncer['dir'] = UPRIGHT
        if bouncer['rect'].left < 0:
            # bouncer has moved past the left side
            if bouncer['dir'] == DOWNLEFT:
                bouncer['dir'] = DOWNRIGHT
            if bouncer['dir'] == UPLEFT:
                bouncer['dir'] = UPRIGHT
        if bouncer['rect'].right > WINDOWWIDTH:
            # bouncer has moved past the right side
            if bouncer['dir'] == DOWNRIGHT:
                bouncer['dir'] = DOWNLEFT
            if bouncer['dir'] == UPRIGHT:
                bouncer['dir'] = UPLEFT

        # draw the bouncer onto the surface
        pygame.draw.rect(windowSurface, WHITE, bouncer['rect'])

        # check if the bouncer has intersected with any food squares.
        for food in foods[:]:
            if bouncer['rect'].colliderect(food):
                #if doRectsOverlap(bouncer['rect'], food):
                foods.remove(food)

        # draw the food
        for i in range(len(foods)):
            pygame.draw.rect(windowSurface, GREEN, foods[i])

        # draw the window onto the screen
        pygame.display.update()
        mainClock.tick(40)
main()
