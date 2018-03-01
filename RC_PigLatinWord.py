#Ruhika Chatterjee
#Python Period 5
#December 2, 2015
#Convert a word into pig latin
#'y' is not used as a vowel
#Assumption: The user enters a word without other characters

def getword ():
    word = input ('Please enter an word in English:')
    return word

def main ():
    word = getword ()
    
    if word [0] in 'aeiou':
        pigword = word [1:] + word [0] + 'way'

    else:
        pigword = word [1:] + word [0] + 'ay'

    print ('The word', word, 'is', pigword, 'in pig latin.')

main()
