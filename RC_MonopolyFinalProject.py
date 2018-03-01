#Ruhika Chatterjee
#Python Period 5
#May 20, 2016
#Final Project- Monopoly

import pygame, sys, random
from pygame.locals import *

WINDOWHEIGHT = 950
WINDOWWIDTH = 950

MOVESPEED = 3

onePlayerPos = 350
twoPlayerPos = 400
threePlayerPos = 450

BLACK = (0,0,0)
WHITE = (255,255,255)

YELLOW = (255, 255, 0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
PURPLE = (153,51,255)

COLORS = [RED, YELLOW, GREEN, BLUE, PURPLE]

CHANCE = ['Advance to Go (Collect $200)','Advance to Illinois Ave-If you pass Go, collect $200', 'Advance to St. Charles Place– If you pass Go, collect $200',
          'Advance token to nearest Utility. If unowned, you may buy it from the Bank.', 'Advance token to the nearest Railroad.', 'Bank pays you dividend of $50',
          'Go Back 3 Spaces', 'Go to Jail– Do not pass Go –Do not collect $200', 'Advance token to nearest Railroad.', 'Pay poor tax of $15',
          'Take a ride on the Reading– If you pass Go, collect $200', 'Take a walk on the Boardwalk',
          'You have been elected Chairman of the Board – Pay each player $50', 'You have won a crossword competition - Collect $100']
#Make general repairs on all your property – For each house pay $25 –For each hotel $100, Your building {and} loan matures – Collect $150

COMMUNITYCHEST = ['Advance to Go (Collect $200)','Bank error in your favor – Collect $200',"Doctor's fees {fee} – Pay $50", 'From sale of stock you get $50',
                  'Go to Jail– Do not pass Go –Do not collect $200', 'Grand Opera Night– Collect $50 from every player for seats',
                  'Holiday Fund matures - Collect $100', 'Income tax refund – Collect $20', 'It is your birthday - Collect $10 from each player', 
                  'Life insurance matures – Collect $100', 'Pay hospital fees of $100', 'Pay school fees of $150', 'Receive $25 consultancy fee', 
                  'You have won second prize in a beauty contest– Collect $10', 'You inherit $100']
#You are assessed for street repairs – $40 per house – $115 per hotel

SPACES = [{'place': 'Go', 'location':pygame.Rect(850,850,100,100), 'price':0, 'owner':None},
          {'place': 'Mediterranean Avenue', 'location':pygame.Rect(766,850,84,100), 'price':60, 'owner':None},
          {'place': 'Community Chest', 'location':pygame.Rect(683,850,83,100), 'price':0, 'owner':None},
          {'place': 'Baltic Avenue', 'location':pygame.Rect(600,850,83,100), 'price':60, 'owner':None},
          {'place': 'Income Tax', 'location':pygame.Rect(516,850,84,100), 'price':'200', 'owner':None},
          {'place': 'Reading Railroad', 'location':pygame.Rect(433,850,83,100), 'price':200, 'owner':None},
          {'place': 'Oriental Avenue', 'location':pygame.Rect(350,850,83,100), 'price':100, 'owner':None},
          {'place': 'Chance', 'location':pygame.Rect(266,850,84,100), 'price':0, 'owner':None},
          {'place': 'Vermont Avenue', 'location':pygame.Rect(183,850,83,100), 'price':100, 'owner':None},
          {'place': 'Connecticut Avenue', 'location':pygame.Rect(100,850,83,100), 'price':120, 'owner':None},
          {'place': 'Jail', 'location':pygame.Rect(0,850,100,100), 'price':0, 'owner':None},
          {'place': 'St. Charles Place', 'location':pygame.Rect(0,766,100,84), 'price':140, 'owner':None},
          {'place': 'Electric Company', 'location':pygame.Rect(0,683,100,83), 'price':150, 'owner':None},
          {'place': 'States Avenue', 'location':pygame.Rect(0,600,100,83), 'price':140, 'owner':None},
          {'place': 'Virginia Avenue', 'location':pygame.Rect(0,516,100,84), 'price':160, 'owner':None},
          {'place': 'Pennsylvania Railraod', 'location':pygame.Rect(0,433,100,83), 'price':200, 'owner':None},
          {'place': 'St. James Place', 'location':pygame.Rect(0,350,100,83), 'price':180, 'owner':None},
          {'place': 'Community Chest', 'location':pygame.Rect(0,266,100,84), 'price':0, 'owner':None},
          {'place': 'Tennessee Avenue', 'location':pygame.Rect(0,183,100,83), 'price':180, 'owner':None},
          {'place': 'New York Avenue', 'location':pygame.Rect(0,100,100,83), 'price':200, 'owner':None},
          {'place': 'Free Parking', 'location':pygame.Rect(0,0,100,100), 'price':'F', 'owner':None},
          {'place': 'Kentucky Avenue', 'location':pygame.Rect(100,0,83,100), 'price':220, 'owner':None},
          {'place': 'Chance', 'location':pygame.Rect(183,0,83,100), 'price':0, 'owner':None},
          {'place': 'Indiana Avenue', 'location':pygame.Rect(266,0,84,100), 'price':220, 'owner':None},
          {'place': 'Illinios Avenue', 'location':pygame.Rect(350,0,83,100), 'price':240, 'owner':None},
          {'place': 'B.&O. Railroad', 'location':pygame.Rect(433,0,83,100), 'price':200, 'owner':None},
          {'place': 'Atlantic Avenue', 'location':pygame.Rect(516,0,84,100), 'price':260, 'owner':None},
          {'place': 'Ventnor Avenue', 'location':pygame.Rect(600,0,83,100), 'price':260, 'owner':None},
          {'place': 'Waterworks', 'location':pygame.Rect(683,0,83,100), 'price':150, 'owner':None},
          {'place': 'Marvin Gerdens', 'location':pygame.Rect(766,0,84,100), 'price':280, 'owner':None}, 
          {'place': 'Go To Jail', 'location':pygame.Rect(850,0,100,100), 'price':0, 'owner':None},
          {'place': 'Pacific Avenue', 'location':pygame.Rect(850,100,100,83), 'price':300, 'owner':None},
          {'place': 'North Carolina Avenue', 'location':pygame.Rect(850,183,100,83), 'price':300, 'owner':None},
          {'place': 'Community Chest', 'location':pygame.Rect(850,266,100,84), 'price':0, 'owner':None},
          {'place': 'Pennsylvania Avenue', 'location':pygame.Rect(850,350,100,83), 'price':320, 'owner':None},
          {'place': 'Short Line Railroad', 'location':pygame.Rect(850,433,100,84), 'price':200, 'owner':None},
          {'place': 'Chance', 'location':pygame.Rect(850,517,100,83), 'price':0, 'owner':None},
          {'place': 'Park Place', 'location':pygame.Rect(850,600,100,83), 'price':350, 'owner':None},
          {'place': 'Luxury Tax', 'location':pygame.Rect(850,683,100,83), 'price':'100', 'owner':None},
          {'place': 'Boardwalk', 'location':pygame.Rect(850,766,100,84), 'price':400, 'owner':None}]

def drawText (text, location, textcolor, backgroundcolor):
    global windowSurface
    
    fontObj = pygame.font.SysFont(None, 20)
    tSurfObj = fontObj.render(text, True, textcolor, backgroundcolor)
    tRectObj = tSurfObj.get_rect()
    tRectObj.center = location
    windowSurface.blit(tSurfObj, tRectObj)

def getNumberOfPlayers ():
    global windowSurface, clicked, onePlayerPos, twoPlayerPos, threePlayerPos, onePlayer, twoPlayer, threePlayer, players, playersChosen
    
    drawText ('How Many Players?', (WINDOWWIDTH/2, 300), WHITE, BLACK)
    drawText ('1', (WINDOWWIDTH/2, onePlayerPos), WHITE, BLACK)
    drawText ('2', (WINDOWWIDTH/2, twoPlayerPos), WHITE, BLACK)
    drawText ('3', (WINDOWWIDTH/2, threePlayerPos), WHITE, BLACK)
    
    if clicked[0] > WINDOWWIDTH/2 - 20 and clicked[0] < WINDOWWIDTH/2 + 20:
        if clicked [1] > onePlayerPos - 20 and clicked[1] < onePlayerPos + 20:    onePlayer = True
        if clicked [1] > twoPlayerPos - 20 and clicked[1] < twoPlayerPos + 20:    twoPlayer = True
        if clicked [1] > threePlayerPos - 20 and clicked[1] < threePlayerPos + 20:    threePlayer = True

    if onePlayer or twoPlayer or threePlayer:
        if onePlayer:   onePlayer = False
        if twoPlayer:
            players += [{'position': 0, 'color': WHITE, 'money':3000, 'properties':[]}]
            twoPlayer = False
        if threePlayer:
            players += [{'position': 0, 'color': WHITE, 'money':3000, 'properties':[]}, {'position': 0, 'color': WHITE, 'money':3000, 'properties':[]}]
            threePlayer = False
        clicked = (0,0)
        playersChosen = True

def getColors ():
    global windowSurface, clicked, players, player, gamePlaying, nextMove
    
    drawText ('For Player: ' + str(player), (WINDOWWIDTH/2, 300), WHITE, BLACK)
    for color in COLORS:
        colorRect = pygame.Rect(WINDOWWIDTH/2-10, 350+(50*COLORS.index(color)), 20, 20)
        pygame.draw.rect (windowSurface, color, colorRect)
        if colorRect.collidepoint(clicked):
            players[player-1]['color'] = color
            if player == len(players):
                gamePlaying = True
                nextMove = True
            else:   player += 1
            clicked = (0,0)

def drawBoard ():
    global windowSurface, boardSImage, board, freeParking, players, diceRoll
    
    windowSurface.blit(boardSImage, board)
    drawText ('Free Parking: ' + str (freeParking), (WINDOWHEIGHT/2, 825), BLACK, WHITE)
    drawText ('Dice: '+str(diceRoll), (WINDOWWIDTH/2,725), BLUE, WHITE)
    
    for aPlayer in players:
        pygame.draw.rect(windowSurface, aPlayer['color'], pygame.Rect(SPACES[aPlayer['position']]['location'].center[0]-10, SPACES[aPlayer['position']]['location'].center[1]-10, 20, 20))

        drawText ('Player: ' + str (players.index(aPlayer)+1), (300 + 100*players.index(aPlayer), 200), BLACK, WHITE)
        drawText ('Money: ' + str (aPlayer['money']), (325 + 100*players.index(aPlayer), 250), BLACK, WHITE)
        drawText ('Properties:', (325 + 100*players.index(aPlayer), 300), BLACK, WHITE)
        for aProperty in aPlayer['properties']:
            drawText (str (SPACES[aProperty]['place']), (325 + 100*players.index(aPlayer), 350+ 25*aPlayer['properties'].index(aProperty)), BLACK, WHITE)

def buyOrRent ():
    global players, playing, spaceHit, rightKey, nextMove, mainClock, SPACES
    
    if SPACES[players[playing]['position']]['owner'] != []:
        drawText ('HIT SPACE IF YOU WANT TO BUY THE PROPERTY, HIT RIGHT ARROW IF NO.', (WINDOWWIDTH/2, 150), RED, WHITE)

        if spaceHit or rightKey:
            if spaceHit:
                players[playing]['properties'] += [players[playing]['position']]
                players[playing]['money'] -= int(SPACES[players[playing]['position']]['price'])
                SPACES[players[playing]['position']]['owner'] = playing
                spaceHit = False
            elif rightKey:    rightKey = False
            
            nextMove = True
            mainClock.tick(50000000)
    else:
        players[playing]['money'] -= SPACES[players[playing]['position']]['price'] / 10
        players[SPACES[players[playing]['position']]['owner']]['money'] += SPACES[players[playing]['position']]['price'] / 10
        nextMove = True

def communityChest ():
    global players, playing, freeParking, mainClock
    
    theMove = random.choice(COMMUNITYCHEST)
    if theMove == 'Advance to Go (Collect $200)':
        players[playing]['position'] = 0
        players[playing]['money'] += 200
    elif theMove == 'Bank error in your favor – Collect $200':  players[playing]['money'] += 200
    elif theMove == "Doctor's fees {fee} – Pay $50":
        players[playing]['money'] -= 50
        freeParking += 50
    elif theMove == 'From sale of stock you get $50':   players[playing]['money'] += 50
    elif theMove == 'Go to Jail– Do not pass Go –Do not collect $200':  players[playing]['position'] = 10
    elif theMove == 'Grand Opera Night– Collect $50 from every player for seats':
        for player in players:
            if player != players[playing]:
                player['money'] -= 50
                players[playing]['money'] += 50
    elif theMove == 'Holiday Fund matures - Collect $100':  players[playing]['money'] += 100
    elif theMove == 'Income tax refund – Collect $20':  players[playing]['money'] += 20
    elif theMove == 'It is your birthday - Collect $10 from each player':
        for player in players:
            if player != players[playing]:
                player['money'] -= 10
                players[playing]['money'] += 10
    elif theMove == 'Life insurance matures – Collect $100':    players[playing]['money'] += 100
    elif theMove == 'Pay hospital fees of $100':
        players[playing]['money'] -= 100
        freeParking += 100
    elif theMove == 'Pay school fees of $150':
        players[playing]['money'] -= 150
        freeParking += 150
    elif theMove == 'Receive $25 consultancy fee':  players[playing]['money'] += 25
    elif theMove == 'You have won second prize in a beauty contest– Collect $10':   players[playing]['money'] += 10
    elif theMove == 'You inherit $100': players[playing]['money'] += 100
    drawText ('Community Chest: ' + theMove, (WINDOWWIDTH/2, 775), BLACK, WHITE)

    mainClock.tick(500000000)

def chance ():
    global players, playing, freeParking, spaceHit, rightKey, mainClock
    
    theMove = random.choice(CHANCE)
    if theMove == 'Advance to Go (Collect $200)':
        players[playing]['position'] = 0
        players[playing]['money'] += 200
    elif theMove == 'Advance to Illinois Ave-If you pass Go, collect $200':
        if players[playing]['position'] > 34 and players[playing]['position'] <= 39: players[playing]['money'] += 200
        players[playing]['position'] = 34
    elif theMove == 'Advance to St. Charles Place– If you pass Go, collect $200':
        if players[playing]['position'] > 11 and players[playing]['position'] <= 39: players[playing]['money'] += 200
        players[playing]['position'] = 11
    elif theMove == 'Advance token to nearest Utility.':
        if players[playing]['position'] > 0 and players[playing]['position'] <= 12: players[playing]['position'] = 12
        elif players[playing]['position'] > 12 and players[playing]['position'] <= 28: players[playing]['position'] = 28
        elif players[playing]['position'] > 28 and players[playing]['position'] <= 39:
            players[playing]['position'] = 12
            players[playing]['money'] += 200
        elif theMove == 'Advance token to the nearest Railroad.':
            if players[playing]['position'] > 5 and players[playing]['position'] <= 15: players[playing]['position'] = 15
            elif players[playing]['position'] > 15 and players[playing]['position'] <= 25: players[playing]['position'] = 25
            elif players[playing]['position'] > 25 and players[playing]['position'] <= 35: players[playing]['position'] = 35
            elif players[playing]['position'] > 35 and players[playing]['position'] <= 39:
                players[playing]['position'] = 5
                players[playing]['money'] += 200
            elif players[playing]['position'] > 0 and players[playing]['position'] <= 5:    players[playing]['position'] = 5
        elif theMove == 'Bank pays you dividend of $50':    players[playing]['money'] += 50
        elif theMove == 'Go Back 3 Spaces': players[playing]['position'] -= 3
        elif theMove == 'Go to Jail– Do not pass Go –Do not collect $200':  players[playing]['position'] = 10
        elif theMove == 'Pay poor tax of $15':
            players[playing]['money'] -= 15
            freeParking += 15
        elif theMove == 'Take a ride on the Reading– If you pass Go, collect $200':
            players[playing]['position'] = 5
            if players[playing]['position'] > 0 and players[playing]['position'] <= 5:  pass
            else:   players[playing]['money'] += 200
        elif theMove == 'Take a walk on the Boardwalk':
            players[playing]['position'] = 39
        elif theMove == 'You have been elected Chairman of the Board – Pay each player $50':
            for player in players:
                if player != players[playing]:
                    players[playing]['money'] -= 50
                    player['money'] += 50
        elif theMove == 'You have won a crossword competition - Collect $100':  players[playing]['money'] += 100

    drawText ('Chance: ' + theMove, (WINDOWWIDTH/2, 775), BLACK, WHITE)
    mainClock.tick(5000000000)

def makeMove():
    global windowSurface, players, playing, SPACES, nextMove, spaceHit, rightKey, freeParking, mainClock
    
    if type(SPACES[players[playing]['position']]['price']) is int and SPACES[players[playing]['position']]['price'] > 0:
        buyOrRent ()
        
    elif SPACES[players[playing]['position']]['price'] != 0:
        print (SPACES[players[playing]['position']]['price'])
        if SPACES[players[playing]['position']]['price'] == 'F':
            players[playing]['money'] += int(freeParking)
            freeParking = 0
        else:
            players[playing]['money'] -= int(SPACES[players[playing]['position']]['price'])
            freeParking += int(SPACES[players[playing]['position']]['price'])

        nextMove = True
        mainClock.tick(100)
    elif SPACES[players[playing]['position']]['price'] == 0:
        if SPACES[players[playing]['position']]['place'] == 'Go':
            players[playing]['money'] += 200
        elif SPACES[players[playing]['position']]['place'] == 'Community Chest':
            communityChest ()
        elif SPACES[players[playing]['position']]['place'] == 'Chance':
            chance ()
        elif SPACES[players[playing]['position']]['place'] == 'Go To Jail':
            players[playing]['position'] = 10

        nextMove = True
        mainClock.tick(500000)

def main():
    global onePlayer, twoPlayer, threePlayer, players, playersChosen, windowSurface, clicked, player, gamePlaying, nextMove, freeParking, playing, nextMove
    global spaceHit, rightKey, boardSImage, board, mainClock, diceRoll

    pygame.init()
    mainClock = pygame.time.Clock()
    
    windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
    pygame.display.set_caption('Monopoly')
    
    board = pygame.Rect (0,0,WINDOWHEIGHT, WINDOWHEIGHT)
    boardImage = pygame.image.load ('monopolyBoard.png')
    boardSImage = pygame.transform.scale (boardImage, (WINDOWHEIGHT, WINDOWHEIGHT))
    
    players = [{'position': 0, 'color': WHITE, 'money':3000, 'properties':[]}]

    clicked = (0,0)
    
    playing = -1

    onePlayer = False
    twoPlayer = False
    threePlayer = False

    playersChosen = False
    player = 1
    
    gameOver = False
    gamePlaying = False

    spaceHit = False
    rightKey = False

    freeParking = 0
    diceRoll = 0
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_SPACE:
                    spaceHit = True
                if event.key == K_RIGHT:
                    rightKey = True
            if event.type == MOUSEBUTTONDOWN:
                clicked = event.pos
        
        windowSurface.fill (BLACK)
        
        if not gameOver:
            if gamePlaying:
                drawBoard ()

                if players[playing]['position'] != 10:
                    if nextMove:
                        if playing == len(players)-1: playing = 0
                        else:   playing += 1
                
                        diceRoll = random.randint (1,6)
                        players[playing]['position'] += diceRoll
                        if players[playing]['position'] >= 40:
                            players[playing]['position'] -= 40
                            players[playing]['money'] += 200 #############
                        nextMove = False
                    
                    makeMove ()

                else:
                    diceRoll = random.randint (1,6)
                    if diceRoll == 6:
                        players[playing]['position'] += 1

                for player in players:
                    if player['money'] == 0:
                        gamePlaying = False

                        drawText ('Game Over', (WINDOWWIDTH/2,WINDOWHEIGHT/2), BLUE, WHITE)
                        mainClock.tick (5000)
            
            else:
                if not playersChosen:
                    getNumberOfPlayers ()

                else:
                    getColors ()
        
        pygame.display.update()
        mainClock.tick(40)

main ()

###
##  Land on own property
##  Check rent
##  print properties correctly
##  pass go
###


##Compress all files into one file for submission
