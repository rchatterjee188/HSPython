#Ruhika Chatterjee
#Python Perion 5
#November 30, 2015
#Replace o with e in a word

def getword ():
    word = input ('Please enter a word:')
    word = word.lower()
    return word

def main ():
    word = getword ()

    if 'o' in word:
        for i in range(len(word)):
            if word[i] == 'o':
                word = word [:i] + 'e' + word [(i + 1):]

    print (word)

main()
