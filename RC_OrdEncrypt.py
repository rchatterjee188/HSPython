#Ruhika Chatterjee
#Python Period 5
#March 4, 2016
#Encrypt data given by user
#Non-letter characters are encrypted.
#Assumption: Characters that have an ordinal less than 91.

def getText ():
    text = '_'
    text = input ('Please enter the string you would like to encrypt: ')
    text = textUpper (text)
    return text

def textUpper (string):
    for i in range(len(string)):
        if string[i].islower():
            letter = string[i].upper()
            string = string[:i] + letter + string[i+1:]
    return string

def getKey (string):
    return ord(string[0]) - 64

def getCipherText (text,key):
    ciphertext = str(ord(text[0]))
    for i in range (len(text)):
        if text[i].isupper():
            encryption = ord(text[i]) + key
            if encryption > ord('Z'):
                encryption -= 26
            elif encryption < ord('A'):
                encryption += 26
            ciphertext += str(encryption)
        else:
            ciphertext += str (ord(text[i]) + key)
    return ciphertext
    

def main ():
    text = getText ()
    key = getKey (text)
    ciphertext = getCipherText (text,key)
    print (ciphertext)

main ()
