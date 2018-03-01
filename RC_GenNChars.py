#Ruhika Chatterjee
#Python Period 5
#September 30, 2015
#Print integer n, c number of times

#ask user for the character and lenght
userChar = input ('Please enter a character:')
stringLen = int ( input ('Please enter a lenght for the string:'))

#initialize variables
fullString = ''
counter = 0

#add a character n to full string c number of times
while counter < stringLen:
    fullString = fullString + userChar
    counter = counter + 1

#print full string
print ('The full string is:', fullString)
