#Ruhika Chatterjee
#Pyhton Period 5
#September 16, 2015
#Find the standard deviation of eight numbers

import math

#get the numbers and convert them into integers
value1 = int(input('Please enter a number:'))
value2 = int(input('Please enter a number:'))
value3 = int(input('Please enter a number:'))
value4 = int(input('Please enter a number:'))
value5 = int(input('Please enter a number:'))
value6 = int(input('Please enter a number:'))
value7 = int(input('Please enter a number:'))
value8 = int(input('Please enter a number:'))

#calculate the mean of the numbers
mean = (value1 + value2 + value3 + value4 + value5 + value6 + value7 + value8) / 8

#find the deviation squared of each number
value1 = (value1 - mean) ** 2
value2 = (value2 - mean) ** 2
value3 = (value3 - mean) ** 2
value4 = (value4 - mean) ** 2
value5 = (value5 - mean) ** 2
value6 = (value6 - mean) ** 2
value7 = (value7 - mean) ** 2
value8 = (value8 - mean) ** 2

#find the mean of the deviations squared
mean = (value1 + value2 + value3 + value4 + value5 + value6 + value7 + value8) / 8

#take the square root to fint the standard deviation
sdeviation = math.sqrt(mean)

#print the standard deviation
print ('The standard deviation is', sdeviation)
