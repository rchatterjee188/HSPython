#Ruhika Chatterjee
#Pyhton Period 5
#September 16, 2015
#Find the mean/average of six numbers

#initialize variables
numcounter = 0
sum1 = 0

#get six numbers from the user, add it to the sum
while numcounter < 6:
    number = int(input('Please enter a number:'))
    sum1 = sum1 + number
    numcounter = numcounter + 1

#calculate the mean
mean = sum1 / 6

#print the mean
print ('The average is', mean)
