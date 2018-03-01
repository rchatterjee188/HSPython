#Ruhika Chatterjee
#Python Period 5
#February 16, 2015
#Simplified Battleship Game
#Assumption: User enters data of the data type requested

#FILL OUT- CHECKLIST AND TEST CASSES
#CHECK TEST CASES AGAIN
#MAGIC NUMBERS

import random, time

BOARDVALS = [1,2,3,4,5,6,7,8,9]

def firstPlayer():
    #Randomly decide who goes first
    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'

def getPlayerBoard ():
    #Get the user's 3 and 2 spot ships and validate the data
    ships = [' '] * 10
    ship3 = [0] * 3
    ship2 = [0] *2
    
    while ship2[0] in ship3 or ship2[1] in ship3:
        ship3 = [0] * 3
        ship2 = [0] *2

        direction3 = 0
        while direction3 not in [1,2]:  direction3 = int (input ('Would you like to place your 3 spot ship horizontally(1) or vertically(2)?:'))
        if direction3 == 1:
            row = 0
            while row not in [1,2,3]:   row = int (input ('Please enter the row you would like to place it in (1-3):'))
            if row == 1:    space = 1
            elif row == 2:  space = 4
            else:  space = 7
            ship3[0] = space
            ship3[1] = space + 1
            ship3[2] = space + 2
        else:
            column = 0
            while column not in [1,2,3]: column = int (input ('Please enter the column you would like to place it in (1-3):'))
            column = int (column)
            ship3[0] = column
            ship3[1] = column + 3
            ship3[2] = column + 6
        
        while ship2[0] not in BOARDVALS or ship2[1] not in BOARDVALS or ship2[0] == ship2[1] or (ship2[0] != ship2[1]+3 and ship2[0] != ship2[1]-3 and ship2[0] != ship2[1]+1 and ship2[0] != ship2[1]-1):
            ship2 = (input ('Would you like to place your 2 spot ship (Enter the two adjacent numbers separated by a space)?:')).split()
            if len (ship2) == 2 and ship2[0].isdigit() and ship2[1].isdigit() and ('3' not in ship2 or '4' not in ship2) and ('6' not in ship2 or '7' not in ship2):
                ship2[0] = int (ship2[0])
                ship2[1] = int (ship2[1])
            else:   ship2 = [0,0]
            
    ships[ship2[0]] = '2'
    ships[ship2[1]] = '2'
    ships[ship3[0]] = '3'
    ships[ship3[1]] = '3'
    ships[ship3[2]] = '3'

    print ()
    return ships

def getCompBoard ():
    #Randomly decide the user's board and validate data
    ships = [' '] * 10
    
    direction3 = random.randint(1,2)    #direction of 3 spot ship #horizontal(1), vertical(2)
    if direction3 == 1:
        row = random.choice([1,4,7])
        ships [row] = '3'
        ships [row + 1] = '3'
        ships [row + 2] = '3'
    else:
        column = random.randint(1,3)
        ships [column] = '3'
        ships [column + 3] = '3'
        ships [column + 6] = '3'
    
    ship2_1 = 0
    ship2_2 = 0
    while not isSpaceFree (ships, ship2_1) or ship2_1 not in BOARDVALS: ship2_1 = random.randint(1,9)
    ships[ship2_1] = '2'
    #goes to next column
    if (ship2_1 + 1) in BOARDVALS and isSpaceFree(ships,(ship2_1 + 1)) and ship2_1 != 3 and ship2_1 != 6:   ship2_2 = ship2_1 + 1
    elif  (ship2_1 + 3) in BOARDVALS and isSpaceFree(ships,(ship2_1 + 3)):  ship2_2 = ship2_1 + 3
    elif  (ship2_1 - 1) in BOARDVALS and isSpaceFree(ships,(ship2_1 - 1)) and ship2_1 != 4 and ship2_1 != 7:    ship2_2 = ship2_1 - 1
    elif (ship2_1 - 3) in BOARDVALS and isSpaceFree(ships,(ship2_1 - 3)):   ship2_2 = ship2_1 - 3
    ships[ship2_2] = '2'
    
    return ships
        
def displayBoard(board):
    print('|   |   |   |')
    print('| ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' |')
    print('|   |   |   |')
    print('-------------')
    print('|   |   |   |')
    print('| ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' |')
    print('|   |   |   |')
    print('-------------')
    print('|   |   |   |')
    print('| ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' |')
    print('|   |   |   |')

def getCompMove(computerMoves, lastHit, shipHit, previousHit):
    #3 4 and 6 7 thing, if hit 2 then 3 vise versa
    #AI to determine where to put the next player move with validaions
    move = 0
    if isSpaceFree (computerMoves, 5):  move = 5
    elif shipHit == 3:
        #Tries to sink ship 3
        if previousHit != 0:
            if lastHit == previousHit+1 and lastHit+1 != 3 and lastHit+1 != 6:
                if lastHit+1 in BOARDVALS and isSpaceFree (computerMoves, lastHit+1):   move = lastHit + 1
                elif previousHit-1 in BOARDVALS and isSpaceFree (computerMoves, previousHit-1):   move = previousHit-1
                else:
                    while not isSpaceFree(computerMoves,move) or move not in BOARDVALS: move = random.choice(BOARDVALS)
            elif lastHit == previousHit+3:
                if lastHit+3 in BOARDVALS and isSpaceFree (computerMoves, lastHit+3):   move = lastHit + 3
                elif previousHit-3 in BOARDVALS and isSpaceFree (computerMoves, previousHit-3):   move = previousHit-3
                else:
                    while not isSpaceFree(computerMoves,move) or move not in BOARDVALS: move = random.choice(BOARDVALS)
            elif lastHit == previousHit-1 and lastHit+1 != 4 and lastHit+1 != 7:
                if lastHit-1 in BOARDVALS and isSpaceFree (computerMoves, lastHit-1):   move = lastHit - 1
                elif previousHit+1 in BOARDVALS and isSpaceFree (computerMoves, previousHit+1):   move = previousHit+1
                else:
                    while not isSpaceFree(computerMoves,move) or move not in BOARDVALS: move = random.choice(BOARDVALS)
            elif lastHit == previousHit-3:
                if lastHit-3 in BOARDVALS and isSpaceFree (computerMoves, lastHit-3):   move = lastHit - 3
                elif previousHit+3 in BOARDVALS and isSpaceFree (computerMoves, previousHit+3):   move = previousHit+3
                else:
                    while not isSpaceFree(computerMoves,move) or move not in BOARDVALS: move = random.choice(BOARDVALS)
            else:
                while not isSpaceFree(computerMoves,move) or move not in BOARDVALS: move = random.choice(BOARDVALS)
        else:
            if lastHit+1 in BOARDVALS and isSpaceFree (computerMoves, lastHit+1): move = lastHit + 1
            elif lastHit+3 in BOARDVALS and isSpaceFree (computerMoves, lastHit+3): move = lastHit + 3
            elif lastHit-1 in BOARDVALS and isSpaceFree (computerMoves, lastHit-1): move = lastHit - 1
            elif lastHit-3 in BOARDVALS and isSpaceFree (computerMoves, lastHit-3): move = lastHit - 3
            else:
                while not isSpaceFree(computerMoves,move) or move not in BOARDVALS: move = random.choice(BOARDVALS)
    elif shipHit == 2:
        #Tries to sink ship 2
        if lastHit+1 in BOARDVALS and isSpaceFree (computerMoves, lastHit+1) and lastHit+1 != 3 and lastHit+1 != 6: move = lastHit + 1
        elif lastHit+3 in BOARDVALS and isSpaceFree (computerMoves, lastHit+3): move = lastHit + 3
        elif lastHit-1 in BOARDVALS and isSpaceFree (computerMoves, lastHit-1) and lastHit+1 != 4 and lastHit+1 != 7: move = lastHit - 1
        elif lastHit-3 in BOARDVALS and isSpaceFree (computerMoves, lastHit-3): move = lastHit - 3
        else:
            while not isSpaceFree(computerMoves,move) or move not in BOARDVALS: move = random.choice(BOARDVALS)
    else:
        while not isSpaceFree(computerMoves,move) or move not in BOARDVALS: move = random.choice(BOARDVALS)
    return move

def getPlayerMove(board):
    #Get player's move and validate data
    move = 0
    while move not in BOARDVALS or not isSpaceFree(board, move):
        move = int(input('What is your next move? (1-9):'))
        print ()
    return move

def makeMoveAndDisplay(move, board, opponentBoard, previousHit, lastHit, turn, shipHit):
    #Make move on board, determine if move is hit/miss/sink and tell user
    if not isSpaceFree(opponentBoard,move):
        board[move] = 'X'
        previousHit = lastHit
        lastHit = move
        
        if opponentBoard[move] == '3':
            opponentBoard[move] = 'H'
            if '3' not in opponentBoard:
                print ('The', turn, 'sank the 3 spot ship!')
                shipHit = 0
            else:
                print ('The', turn, 'hit the 3 spot ship!')
                shipHit = 3
        elif opponentBoard[move] == '2':
            opponentBoard[move] = 'H'
            if '2' not in opponentBoard:
                print ('The', turn, 'sank the 2 spot ship!')
                shipHit = 0
            else:
                print ('The', turn, 'hit the 2 spot ship!')
                shipHit = 2
    else:
        board[move] = 'M'
        print ('The', turn, 'missed!')
    return board, opponentBoard, lastHit, shipHit, previousHit

def isSpaceFree(board, move):
    #Returns boolean if space is free
    return board[move] == ' '

def isWinner(opponentBoard):
    #Determine if the player won
    return '3' not in opponentBoard and '2' not in opponentBoard

def playAgain():
    #Ask user if they want to play again
    return input('Do you want to play again? (yes/no)').lower().startswith('y')

def main ():
    print ("Hi! Welcome to Battleship, place your ship then try to hit the computer's ships.")
    while True:
        turn = firstPlayer ()
        playerHitBoard = [' '] * 10
        compHitBoard = [' '] * 10
        previousPlayerHit = 0    #Hit before last hit
        previousCompHit = 0    #Hit before last hit
        lastPlayerHit = 0
        lastCompHit = 0
        compShipHit = 0
        playerShipHit = 0

        #Intro/welcome
        print('The ' + turn + ' will go first.')
        print ('The board spaces are:')
        displayBoard (['0','1','2','3','4','5','6','7','8','9'])
        print ()

        #Get Boards
        playerShipBoard = getPlayerBoard ()
        displayBoard(playerShipBoard)
        print ()
        compShipBoard = getCompBoard ()
        
        while True:
            if turn == 'player':
                #Player's turn
                print ('-----USER-----')
                displayBoard (playerHitBoard)
                print ()
                move = getPlayerMove (playerHitBoard)
                playerHitBoard,compShipBoard,lastPlayerHit,compShipHit,previousPlayerHit = makeMoveAndDisplay (move,playerHitBoard,compShipBoard,previousPlayerHit,lastPlayerHit,turn,compShipHit)
                print ()
                
                if isWinner(compShipBoard):
                    displayBoard(playerHitBoard)
                    print ()
                    print('Hooray! You have won the game!')
                    break
                else:
                    turn = 'computer'
            
            else:
                #Computer's turn
                move = getCompMove (compHitBoard,lastCompHit, playerShipHit, previousCompHit)
                print ('-----COMP-----')
                compHitBoard,playerShipBoard,lastCompHit,playerShipHit,previousCompHit = makeMoveAndDisplay(move,compHitBoard,playerShipBoard,previousCompHit,lastCompHit,turn,playerShipHit)
                
                displayBoard (compHitBoard)
                print ()
                
                if isWinner(playerShipBoard):
                    print('The computer has beaten you! You lose.')
                    break
                else:
                    turn = 'player'
        
        if not playAgain ():
            #Check if user wants to play again if game is done.
            print ('Thanks for playing Battleship. Goodbye!')
            break
        print ()

main ()

