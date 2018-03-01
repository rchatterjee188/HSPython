def main ():
    playerCounter = 0
    board = [[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' '],[' ',' ',' ',' ',' ',' ',' ']]
    gameDone = False
    while True:
        displayBoard (board)
        print ()
        column = getColumn(playerCounter)
        board = columnInList (board,playerCounter,column) #Put 'R' or 'Y' in board in correct spot
        playerCounter = playerCounter + 1

        gameOver = checkWin (board)
        
        if gameDone:
            if playAgain ():
                playerCounter = 0
                board = [[],[],[],[],[],[],[]]
                gameDone = False
            else:
                break
