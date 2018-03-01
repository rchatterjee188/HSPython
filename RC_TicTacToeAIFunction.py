#Ruhika Chatterjee
#Python Period 5
#January 6, 2015
#Tic Tac Toe AI

import random

def getComputerMove(board, computerLetter):
    if board[5] == ' ':
        move = 5
    elif checkCompChar(board, computerLetter) != 0:
        move = checkCompChar(board, computerLetter)
    elif checkPlayerChar(board, computerLetter) != 0:
        move = checkPlayerChar(board, computerLetter)
    elif ' ' in (board[1] + board[3] + board [7] + board [9]):
        move = random.choice (1,3,7,9)
    else:
        move = random.choice (2,4,6,8)
    return move

def checkCompChar(board, computerLetter):
    move = checkVertical (board, computerLetter)
    if move == 0:
        move = checkHorizontal (board, computerLetter)
    if move == 0:
        move = checkDiagonal (board, computerLetter)
    return move

def checkPlayerChar(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    elif computerLetter == 'O':
        playerLetter = 'X'
    
    move = checkVertical (board, playerLetter)
    if move == 0:
        move = checkHorizontal (board, playerLetter)
    if move == 0:
        move = checkDiagonal (board, playerLetter)
    return move

def checkVertical (board, letter):
    if board [1] == letter and board [4] == letter:
        return 7
    elif board [1] == letter and board [7] == letter:
        return 4
    elif board [4] == letter and board [7] == letter:
        return 1
    elif board [2] == letter and board [5] == letter:
        return 8
    elif board [2] == letter and board [8] == letter:
        return 5
    elif board [5] == letter and board [8] == letter:
        return 2
    elif board [3] == letter and board [6] == letter:
        return 9
    elif board [3] == letter and board [9] == letter:
        return 6
    elif board [6] == letter and board [9] == letter:
        return 3
    else:
        return 0

def checkHorizontal (board, letter):
    if board [1] == letter and board [2] == letter:
        return 3
    elif board [1] == letter and board [3] == letter:
        return 2
    elif board [2] == letter and board [3] == letter:
        return 1
    elif board [4] == letter and board [5] == letter:
        return 6
    elif board [4] == letter and board [6] == letter:
        return 5
    elif board [5] == letter and board [6] == letter:
        return 4
    elif board [7] == letter and board [8] == letter:
        return 9
    elif board [7] == letter and board [9] == letter:
        return 8
    elif board [8] == letter and board [9] == letter:
        return 7
    else:
        return 0

def checkDiagonal (board, letter):
    if board [3] == letter and board [5] == letter:
        return 7
    elif board [3] == letter and board [7] == letter:
        return 5
    elif board [5] == letter and board [7] == letter:
        return 3
    elif board [1] == letter and board [5] == letter:
        return 9
    elif board [1] == letter and board [9] == letter:
        return 5
    elif board [5] == letter and board [9] == letter:
        return 1
    else:
        return 0

def isSpaceFree(board, move):
    # Return true if the passed move is free on the passed board.
    return board[move] == ' '


def drawBoard(board):
    # This function prints out the board that it was passed.

    # "board" is a list of 10 strings representing the board (ignore index 0)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')
    
def main():
    #test the AI
    computerSymbol = 'O'
    #hardcode the board at a point in the game (examples below)
    #computerBoard =  [' ', 'X', 'O', 'X', ' ', ' ', ' ', ' ', ' ', ' ']
    #computerBoard = [' ', 'X', ' ', ' ', 'X', ' ', ' ', 'O', ' ', ' ']
    computerBoard = [' ', ' ', ' ', ' ', 'O', 'X', 'X', 'O', 'X', ' ']
    #what are other board scenarios (game states) that should be tested?
    computerBoard = [' ', ' ', 'O', 'X', ' ', 'X', ' ', 'O', ' ', ' ']
    
    nextCompMove = getComputerMove(computerBoard, computerSymbol)
    drawBoard(computerBoard)
    print("The next computer move should be:", nextCompMove)

main()
