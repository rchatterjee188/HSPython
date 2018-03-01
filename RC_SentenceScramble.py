#Ruhika Chatterjee
#Python Period 5
#November 16, 2015
#Scramble up a sentence.

def everyother (sentence):
    for x in range (0, len(sentence), 2):
        print (sentence [x], end = ' ')
    print ()

def backwards (sentence):
    for x in range (len(sentence) - 1, -1, -1):
        print (sentence [x], end = ' ')
    print()

def firstandsecond (sentence):
    first = sentence[0][0:3]
    second = sentence [1][-3:]
    print (first, '%', second)

def main ():
    sent = input ('Please enter a sentence:')
    sent = sent.split()

    everyother (sent)
    backwards(sent)
    firstandsecond(sent)

main()
