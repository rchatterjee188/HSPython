#Ruhika Chatterjee
#Pyhton Period 5
#October 11, 2015
#Find the factorial of a number

number = int (input ('Please enter a number:'))
nextnum = 1
factorial = 1

for x in range (number):
    factorial = factorial * nextnum
    nextnum = nextnum + 1

print ('The factorial of', number, 'is', factorial)
print ('Goodbye')
