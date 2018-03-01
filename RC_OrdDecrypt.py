#Ruhika Chatterjee
#Python Period 5
#March 9, 2016
#Decrypt a string of numbers.
#Assumption: User enters characters that are already encrypted.

def getData ():
    ciphertext = '_'
    ciphertext = input ('Please enter the string of numbers you would like to decrypt: ')
    return ciphertext

def getKey (encryptedLetter):
    return encryptedLetter - 64

def getPlainText (cipherText,key):
    plainText = ''
    for i in range (2, len(cipherText), 2):
        encryption = int(cipherText[i:i+2]) - key
        if chr(encryption+key).isupper():
            if encryption > ord('Z'):
                encryption -= 26
            elif encryption < ord('A'):
                encryption += 26
        plainText += chr(encryption)
    return plainText

def main ():
    ciphertext = getData ()
    key = getKey (int(ciphertext[0:2]))
    plainText = getPlainText (ciphertext,key)
    print (plainText)

main ()
