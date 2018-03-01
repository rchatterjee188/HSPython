#Ruhika Chatterjee
#Python Period 5
#December 2, 2015
#Convert a word into pig latin
#'y' is not used as a vowel
#Assumption: The user enters a word without other characters (except ' ')

def getphrase ():
    phrase = input ('Please enter an phrase in English:')
    return phrase

def convertphrase (phrase):
    while True:
        for x in range (len (phrase)):
            if phrase [x] == ' ' or x == (len (phrase) - 1):
                if phrase [0] in 'aeiou':
                    if x != (len (phrase) - 1):
                        pigword = phrase [1:x] + phrase [0] + 'way'
                    else:
                        pigword = phrase [1:] + phrase [0] + 'way'
                else:
                    if x != (len (phrase) - 1):
                        pigword = phrase [1:x] + phrase [0] + 'ay'
                    else:
                        pigword = phrase [1:] + phrase [0] + 'ay'
                phrase = phrase [x+1:]
                return pigword, phrase
        
def main ():
    phrase = getphrase ()
    pigphrase = ''
    
    while True:
        pigword, phrase = convertphrase (phrase)
        pigphrase = pigphrase + ' ' + pigword
        if phrase == '':
            break
    
    print ('The phrase is' + pigphrase, 'in pig latin.')

main()
