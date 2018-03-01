#Ruhika Chatterjee
#Pyhton Period 5
#September 24, 2015
#Find the mean/average of two numbers and repeat if user sais so.

yesNo = 'y'

while yesNo == 'y' or yesNo == 'Y':
    #gets the first number and converts into an integer
    print ('Please type a numeric value:')
    value1 = input()
    value1 = int(value1)
    
    #gets the second number and converts into an integer
    print ('Please type another numeric value:')
    value2 = input()
    value2 = int(value2)
    
    #calculates the mean
    mean = (value1 + value2) / 2
    
    #prints the average
    print ('The average is', mean)
    
    yesNo = str (input ('Do you want to try again(y/n)?:'))

print ('Goodbye')
