#Ruhika Chatterjee
#Python Period 5
#November 3, 2015
#A story with a chance ending

import random
import time

def intro():
    print ('You are in a Hogwarts during the Battle of Hogwarts.')
    print ('You hear that Voldemort has gotten into the castle, but')
    print ('you know that your best mate is battling Bellatrix outside.')
    print ()

def wheretogo():
    place = ''
    while place != 'Castle' and place != 'castle' and place != 'Grounds' and place != 'grounds':
        print('Where will you go? (Castle or Grounds)')
        place = input()
                                                        
    return place

def inCastle():
    print('You enter the castle...')
    time.sleep (2)
    print('In front of you, there are two cloaked figures battling')
    print('each other. One person is a friend, and one is a foe.')
    print()

def persontokill():
    kill = ''
    while kill != '1' and kill != '2':
        print('Who will you perform the Avada Kedavra curse on? (1 or 2)')
        kill = input()

    return kill

def checkperson(person):
    print('You perform the curse...')
    time.sleep(2)
    print('The curse hits the figure...')
    time.sleep(2)
    print('The person hits the floor!')
    time.sleep(2)
    print ('The hood falls back and...')
    print()
    time.sleep(2)

    friend = random.randint(1, 2)

    if person == str(friend):
         print('You have just killed your best mate.')
    else:
         print('You have murdered Voldemort!')

def inGrounds ():
    print ('you go towards the gates, where your best mate is')
    time.sleep (2)
    print ('You see a person lying on the ground, dead.')
    time.sleep (2)
    print ('You pull back their hood, and it is your best mate.')
    time.sleep (2)
    print ('You see two people running away. One is Bellatrix who')
    print ('killed your best mate and the other is a friend.')
    print ()

def whotokill():
    kill = ''
    while kill != '1' and kill != '2':
        print('Who will you perform the Avada Kedavra curse on? (1 or 2)')
        kill = input()

    return kill

def isitperson(person):
    print('You perform the curse...')
    time.sleep(2)
    print('The curse hits the figure...')
    time.sleep(2)
    print('The person hits the floor!')
    time.sleep(2)
    print ('The hood falls back and...')
    print()
    time.sleep(2)

    friend = random.randint(1, 2)

    if person == str(friend):
         print('You have just killed Molly Weasley')
    else:
         print('You have murdered Bellatrix!')

def main():
    playAgain = 'yes'
    while playAgain == 'yes' or playAgain == 'y':

        intro()
        where = wheretogo()

        if where == 'Castle' or where == 'castle':
            inCastle()
            person = persontokill()
            checkperson(person)
        else:
            inGrounds()
            person = whotokill()
            isitperson (person)

        print('Do you want to play again? (yes or no)')
        playAgain = input()
        
main()
