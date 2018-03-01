#Ruhika Chatterjee
#Python Period 5
#February 16, 2015
#Simplified Battleship Game
#Assumption: User enters data of the data type requested

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
    
    while True:
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
        
        while True:
            print ()
            ship2 = (input ('Would you like to place your 2 spot ship (Enter the two adjacent numbers separated by a space)?:')).split()
            if len(ship2) == 2 and ship2[0].isdigit() and ship2[1].isdigit():
                ship2[0] = int (ship2[0])
                ship2[1] = int (ship2[1])
                
                if ship2[0] not in BOARDVALS or ship2[1] not in BOARDVALS:  print ('One or more of the values are not in the board.')
                elif ship2[0] == ship2[1]:  print ('The two places overlap.')
                elif (ship2[0] != ship2[1]+3 and ship2[0] != ship2[1]-3 and ship2[0] != ship2[1]+1 and ship2[0] != ship2[1]-1) or (3 in ship2 and 4 in ship2) or (6 in ship2 and 7 in ship2):
                    print ('The two spots are not adjacent.')
                else:   break
            
            else:   print ('Please enter two numbers.')

        if ship2[0] in ship3 or ship2[1] in ship3:
            print ('The ships overlap.')
            print ()
        else:   break
            
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

def getCompMove (compHitBoard, ship2LastHit, ship3LastHit, ship3PreviousHit):
    #AI to determine where to put the next player move with validaions
    move = 0
    if isSpaceFree (compHitBoard, 5):    move = 5	#Empty state
    elif ship3LastHit != 0:	#If 3 ship was hit
        
        if ship3PreviousHit != 0:		#Two spots were hit
            if ship3LastHit == ship3PreviousHit + 1:
                if ship3LastHit+1 in BOARDVALS and isSpaceFree (compHitBoard, ship3LastHit+1): move =  ship3LastHit+1
                elif ship3PreviousHit-1 in BOARDVALS and isSpaceFree(compHitBoard, ship3PreviousHit-1) and ship3LastHit != 3 and ship3LastHit != 6:    move = ship3PreviousHit-1
                else:
                    while isSpaceFree(compHitBoard, move) or move not in BOARDVALS:   move = random.choice (BOARDVALS)
            elif ship3LastHit == ship3PreviousHit + 3:
                if ship3LastHit+3 in BOARDVALS and isSpaceFree (compHitBoard, ship3LastHit+3): move =  ship3LastHit+3
                elif ship3PreviousHit-3 in BOARDVALS and isSpaceFree (compHitBoard, ship3PreviousHit-3):   move = ship3PreviousHit-3
                else:
                    while isSpaceFree(compHitBoard, move) or move not in BOARDVALS:   move = random.choice (BOARDVALS)
            elif ship3LastHit == ship3PreviousHit - 1:
                if ship3LastHit-1 in BOARDVALS and isSpaceFree (compHitBoard, ship3LastHit-1) and ship3LastHit !=4 and ship3LastHit != 7:    move =  ship3LastHit-1
                elif ship3Prev+1 in BOARDVALS and isSpaceFree(compHitBoard, ship3Prevt+1):    move = previousHit+1
                else:
                    while isSpaceFree(compHitBoard, move) or move not in BOARD:   move = random.choice (BOARDVALS)
            elif ship3LastHit == ship3PreviousHit - 3:
                if ship3LastHit-3 in BOARDVALS and isSpaceFree (compHitBoard, ship3LastHit-3):  move =  ship3LastHit-3
                elif ship3PreviousHit+3 in BOARDVALS and isSpaceFree(compHitBoard, ship3PreviousHit+3):    move = ship3PreviousHit+3
                else:
                    while isSpaceFree(compHitBoard, move) or move not in BOARDVALS:   move = random.choice (BOARDVALS)
            else:
                while isSpaceFree(compHitBoard, move) or move not in BOARDVALS:   move = random.choice (BOARDVALS)
                
        else:   #One spot was hit
            if ship3LastHit+1 in BOARDVALS and isSpaceFree (compHitBoard, ship3LastHit+1) and ship2LastHit != 3 and ship2LastHit+1 != 6: move = ship3LastHit + 1
            elif ship3LastHit+3 in BOARDVALS and isSpaceFree (compHitBoard, ship3LastHit+3): move = ship3LastHit + 3
            elif ship3LastHit-1 in BOARDVALS and isSpaceFree (compHitBoard, ship3LastHit-1) and ship2LastHit+1 != 4 and ship2LastHit+1 != 7: move = ship3LastHit - 1
            elif ship3LastHit-3 in BOARDVALS and isSpaceFree (compHitBoard, ship3LastHit-3): move = ship3LastHit - 3
            else:
                while not isSpaceFree(compHitBoard,move) or move not in BOARDVALS: move = random.choice(BOARDVALS)   
    
    
    elif ship2LastHit != 0: #If 2 ship was hit
        if ship2LastHit+1 in BOARDVALS and isSpaceFree (compHitBoard, ship2LastHit+1) and ship2LastHit != 3 and ship2LastHit != 6: move = ship2LastHit + 1
        elif ship2LastHit+3 in BOARDVALS and isSpaceFree (compHitBoard, ship2LastHit+3): move = ship2LastHit + 3
        elif ship2LastHit-1 in BOARDVALS and isSpaceFree (compHitBoard, ship2LastHit-1) and ship2LastHit != 4 and ship2LastHit != 7: move = ship2LastHit - 1
        elif ship2LastHit-3 in BOARDVALS and isSpaceFree (compHitBoard, ship2LastHit-3): move = ship2LastHit - 3
        else:
            while not isSpaceFree(compHitBoard,move) or move not in BOARDVALS: move = random.choice(BOARDVALS)

    
    else:   #Board not empty and no ships hit/ship sunk
        while not isSpaceFree(compHitBoard,move) or move not in BOARDVALS: move = random.choice(BOARDVALS)
        
    return move

def getPlayerMove(board):
    #Get player's move and validate data
    move = 0
    while move not in BOARDVALS or not isSpaceFree(board, move):
        move = int(input('What is your next move? (1-9):'))
        print ()
    return move

def makeMoveAndDisplay(move, board, opponentBoard, turn, ship2LastHit, ship3LastHit, ship3PreviousHit):
    #Make move on board, determine if move is hit/miss/sink and tell user
    if not isSpaceFree(opponentBoard,move):
        board[move] = 'X'
        if opponentBoard[move] == '3':
            opponentBoard[move] = 'H'
            if '3' not in opponentBoard:
                print ('The', turn, 'sank the 3 spot ship!')
                ship3LastHit = 0
                ship3PreviousHit = 0
            else:
                print ('The', turn, 'hit the 3 spot ship!')
                ship3PreviousHit = ship3LastHit
                ship3LastHit = move
        elif opponentBoard[move] == '2':
            opponentBoard[move] = 'H'
            if '2' not in opponentBoard:
                print ('The', turn, 'sank the 2 spot ship!')
                ship2LastHit = 0
            else:
                print ('The', turn, 'hit the 2 spot ship!')
                ship2LastHit = move
    else:
        board[move] = 'M'
        print ('The', turn, 'missed!')
    return board, opponentBoard, ship2LastHit, ship3LastHit, ship3PreviousHit

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
    print ('The board spaces are:')
    displayBoard (['0','1','2','3','4','5','6','7','8','9'])
    print ()
    while True:
        turn = firstPlayer ()
        playerHitBoard = [' '] * 10
        compHitBoard = [' '] * 10
        ship2LastHit = 0
        ship3LastHit = 0
        ship3PreviousHit = 0
        usership2LastHit = 0
        usership3LastHit = 0
        usership3PreviousHit = 0

        #Intro/welcome
        print('The ' + turn + ' will go first.')
        print ()

        #Get Boards
        playerShipBoard = getPlayerBoard ()
        displayBoard(playerShipBoard)
        print ()
        compShipBoard = getCompBoard ()

        time.sleep (2)
        
        while True:
            if turn == 'player':
                #Player's turn
                print ('-----USER-----')
                displayBoard (playerHitBoard)
                print ()
                move = getPlayerMove (playerHitBoard)
                playerHitBoard,compShipBoard, usership2LastHit, usership3LastHit, usership3PreviousHit = makeMoveAndDisplay (move,playerHitBoard,compShipBoard,turn, usership2LastHit, usership3LastHit, usership3PreviousHit)
                print ()
                
                if isWinner(compShipBoard):
                    displayBoard(playerHitBoard)
                    print ()
                    print('Hooray! You have won the game!')
                    break
                else:
                    turn = 'computer'
                
                time.sleep (2)
            
            else:
                #Computer's turn
                move = getCompMove (compHitBoard,ship2LastHit, ship3LastHit, ship3PreviousHit)
                print ('-----COMP-----')
                compHitBoard,playerShipBoard, ship2LastHit, ship3LastHit, ship3PreviousHit = makeMoveAndDisplay(move,compHitBoard,playerShipBoard,turn, ship2LastHit, ship3LastHit, ship3PreviousHit)
                
                displayBoard (compHitBoard)
                print ()
                
                if isWinner(playerShipBoard):
                    print('The computer has beaten you! You lose.')
                    break
                else:
                    turn = 'player'
                
                time.sleep (2)
        
        if not playAgain ():
            #Check if user wants to play again if game is done.
            print ('Thanks for playing Battleship. Goodbye!')
            break
        print ()

main ()

