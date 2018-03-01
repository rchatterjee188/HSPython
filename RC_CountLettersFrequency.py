#Ruhika Chatterjee
#Python Period 5
#January 15, 2016
#Count frequencies of lower case letters.

NUMOFLETTERS = 26
LETTERS = 'abcdefghijklmnopqrstuvwxyz'
TEXT = "… remember, the brick walls are there for a reason. The brick walls are not there to keep us out. The brick walls are there to give us a chance to show how badly we want something. Because the brick walls are there to stop the people who don't want it badly enough. … [H]ave something to bring to the table, … because that will make you more welcome."

def addFrequency (frequency):
    for i in range (len(TEXT)):
        if TEXT[i].isalpha() and TEXT[i].islower():
            x = LETTERS.find(TEXT[i])
            frequency[x] += 1
    return frequency

def printHistogram (frequency):
    for x in range (NUMOFLETTERS):
        print (LETTERS[x], '* ' * int(frequency[x]))

def main ():
    frequency = [0] * NUMOFLETTERS
    
    frequency = addFrequency (frequency)
    
    print ('The text is "' + TEXT + '"')
    printHistogram (frequency)

main ()
