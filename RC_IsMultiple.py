#Ruhika Chatterjee
#Pyhton Period 5
#September 16, 2015
#Find out if the second entered number is a multiple of the first

#get the numbers and converts into integers
value1 = int(input('Please enter a number:'))
value2 = int(input('Please enter a number:'))

#calculate and print if value2 is a multiple of value1
if (value2 % value1) == 0:
    print (value2, 'is a multiple of', value1)
else:
    print (value2, 'is not a multiple of', value1)

