#Ruhika Chatterjee
#Python Period 5
#November 21, 2015
#Create a version of Wheel of Fortune

import random

PHRASES = ['act your age', 'peter piper picks peppers', 'you know the saying', 'hakuna matata', "it's a small world after all"]
PRISES = ['Hogwarts', 'Miami Beach', 'California', "Scotland's Highlands", 'London', 'The Pyramids of Egypt']
NUMOFGUESSES = 5

def randomphrase ():
    #Chooses a random phrase form PHRASES and returns it
    phraseindex = random.randint (0, len(PHRASES) - 1)
    return PHRASES [phraseindex]

def displayboard (missedletters, guessedletters, phrase):
    #prints the missed letters and board with correct letters
    print ('Missed Letters:', end = ' ')
    for letter in missedletters:
        print (letter, end = ' ')
    print()

    spaces = '_' * len(phrase)

    for x in range (len(phrase)):
        if phrase[x] in guessedletters or phrase [x] not in 'abcdefghijklmnopqrstuvwxyz':
            spaces = spaces [:x] + phrase[x] + spaces [x+1:]
        elif phrase [x] == ' ':
            spaces = spaces [:x] + ' ' + spaces [x+1:]

    for letters in spaces:
        print (letters, end = ' ')
    print ('')
    print ('')

def getguess (guessed):
    #get guess from user and validate data
    while True:
        guessletter = input ('Please enter a letter:')
        guessletter = guessletter.lower()
        if guessletter in guessed:
            print ('This letter has alreaty been entered.')
        elif len(guessletter) > 1:
            print ('Please enter a SINGLE letter.')
        elif guessletter not in 'abcdefghijklmnopqrstuvwxyz':
            print ('Please enter a LETTER.')
        else:
            return guessletter

def randomprize ():
    #Chooses a random prize form PPRISES and returns it
    prizeindex = random.randint (0, len(PRISES) - 1)
    return PRISES [prizeindex]

def playagain ():
    #ask user if they want to play again and return a boolean if input starts with y
    print ('Do you want to play again? (yes/no):')
    return input().lower().startswith('y')

def main ():
    #Initialize variables and print welcome
    phrase = randomphrase ()
    print ('Welcome to Wheel of Fortune!')
    print ('Please enter a letter. If it is in the phrase, it will appear on the board.')
    print ('You only get 5 incorect guesses.')
    print ()
    correctletters = ''
    missedletters = ''
    gameisdone = False

    #loop to run till user wins or looses
    while True:
        #print board and get guess
        displayboard (missedletters,correctletters,phrase)
        guess = getguess (correctletters + missedletters)
        
        
        #add letter to correct letters or missed letters and check if user entered all the letters (won). If won, ends game
        if guess in phrase:
            correctletters = correctletters + guess
            print ('Correct!')
            
            foundletters = True
            for z in range(len(phrase)):
                if phrase[z] not in correctletters and phrase[z] in 'abcdefghijklmnopqrstuvwxyz':
                    foundletters = False
                    break
            
            if foundletters:
                gameisdone = True
                prize = randomprize ()
                print ()
                print ("That's correct! The secret phrase is '" + phrase + "'.")
                print ('Congratulations! you won a trip to', prize + '!')
        else:
            missedletters = missedletters + guess
            print ('Incorrect')
        
        #check if user entered more than 5 incorrect guesses (lost)
        if len(missedletters) == NUMOFGUESSES:
            gameisdone = True
            displayboard (missedletters,correctletters,phrase)
            print ('You have guessed 5 letters incorrectly. You lost.')
            print ("The secret phrase was '" + phrase + "'.")
        
        #if user won/lost, ask user if they want to play again, if yes, reset variables, if false, end game
        if gameisdone:
            if playagain():
                phrase = randomphrase ()
                print ('Welcome to Wheel of Fortune!')
                correctletters = ''
                missedletters = ''
                gameisdone = False
            else:
                break

main()
