#Ruhika Chatterjee
#Python Period 5
#November 15, 2015
#Create a madlibs to form random sentences.

import random

ADJECTIVES = 'warm mushy blinding fluffy freezing spicy bitter lemony greasy flaky shrill hushed bright scrawny immense rotund abrasive' .split()
ADVERBS = 'beautifully sorrowfully delightfully abruptly really wickedly sloppily often always lazily only almost sleepily literally completely lively attentively' .split()
NOUNS = 'friends bananas rain-drops trains phones witches pictures houses railroads kneecaps lives tablecloths walnuts pizzas pens books rattlesnakes'. split()
VERBS = 'swims under, flies into, runs over, exclaims with, persues, cries with, sleeps on, eats, programs, sais "hi" to, dictates to, boils over with, relaxes with the sound of, thunders to irratate, jumps on, skips over, tricks' .split(',')
EXCLAMATIONS = 'Wow! Ow! Omg! Oh! Yuck! Gross! Ooooo! Duh! Well! Darn! Shoot! Aaah! So! No! Yes! Ha! Aha!' .split() #Good
NUMBERS = '947 943857 194875 1938475 16 3 0 2 18744370 387474 3842 2038457494 48 77 -5 0.5 1/67' .split() #Good
COLORS = 'black blue green red purple orange white rainbow-colored teal lime laveder yellow grey pink indigo maroon brown' .split() #GOOD
NAMES = 'Fred George Fransis Mary Ron Hermione Donald Robert John Ben Emily Greer Ailee Kenna Lola Bash Catherine' .split() #Good

def calcindexes ():
    Adj = random.randrange (0, len(ADJECTIVES) - 1)
    Adv = random.randrange (0, len(ADVERBS) - 1)
    Nou = random.randrange (0, len(NOUNS) - 1)
    Ver = random.randrange (0, len(VERBS) - 1)
    Exc = random.randrange (0, len(EXCLAMATIONS) - 1)
    Num = random.randrange (0, len(NUMBERS) - 1)
    Col = random.randrange (0, len(COLORS) - 1)
    Nam = random.randrange (0, len(NAMES) - 1)

    sentence = [ADJECTIVES[Adj], ADVERBS[Adv], NOUNS[Nou], VERBS[Ver], EXCLAMATIONS[Exc], NUMBERS[Num], COLORS[Col], NAMES[Nam]]

    return sentence

def main ():
    yesNo = 'yes'
    while yesNo == 'Yes' or yesNo == 'yes':
        sent = calcindexes ()

        print (sent[-1], sent[1] + sent[3], sent[-3], sent[-2], sent[0], sent[2] + '.', sent[-4])
        yesNo = input ('Do you want to play again? (yes or no):')

main ()
