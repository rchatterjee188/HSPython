#Ruhika Chatterjee
#Python Period 5
#March 11, 2016
#Use the Symbol Cipher to encrypt/decrypt a message
#Assumption: User enters string with 4+ letters

import math

ENCRYPTKEYS = {'A':'@', 'E':'=', 'I':'!', 'J':'?', 'O':'*', 'P':'#', 'R':'&', 'S':'$', 'T':'+', 'V':'^', 'X':'%', ' ':'_'}
DECRYPTKEYS = {'@':'A', '=':'E', '!':'I', '?':'J', '*':'O', '#':'P', '&':'R', '$':'S', '+':'T', '^':'V', '%':'X', '_':' '}

def getText ():
    process = ' '
    while process != 'e' and process != 'd':    process = input('Would you like to encrypt or decrypt a message?')[0].lower()
    if process == 'e':
        text = input('Please enter the string you would like to encrypt:')
        text = removeSpaces(text)
        text = upperCase (text)
        
    else:
        text = input('Please enter the string of symobols you would like to decrypt:')
        text = removeSpaces(text)
    return process, text

def removeSpaces (text):
    text = text.strip()
    return text

def upperCase (text):
    for i in range(len(text)):
        text = text[:i] + text[i].upper() + text[i+1:]
    return text

def getEncryption (text):
    for i in range(len(text)):
        if text[i] in ENCRYPTKEYS.keys():
            text = text[:i] + ENCRYPTKEYS[text[i]] + text[i+1:]
    
    halfIndex = math.ceil(len(text)/2)

    text = text[halfIndex:] + text[:halfIndex]

    text = text[-2:] + text[2:-2] + text[:2]
    
    text = text[:halfIndex-2] + text[halfIndex:halfIndex+2] + text[halfIndex-2:halfIndex] + text[halfIndex+2:]
    
    return text

def getDecryption (text):
    halfIndex = math.ceil(len(text)/2)
    text = text[:halfIndex-2] + text[halfIndex:halfIndex+2] + text[halfIndex-2:halfIndex] + text[halfIndex+2:]

    text = text[-2:] + text[2:-2] + text[:2]

    halfIndexLower = math.ceil(len(text)/2)
    text = text[halfIndexLower:] + text[:halfIndexLower]

    for i in range(len(text)):
        if text[i] in DECRYPTKEYS.keys():
            text = text[:i] + DECRYPTKEYS[text[i]] + text[i+1:]
    
    for i in range(len(text)):
        text = text[:i] + text[i].lower() + text[i+1:]

    return text

def main():
    process, text = getText()
    if process == 'e':
        encryptedText = getEncryption (text)
        print (encryptedText)
    else:
        decryptedText = getDecryption (text)
        print (decryptedText)

main()
