#Ruhika Chatterjee
#Python Period 5
#October 11, 2015
#Add the numbers between and including x and y.

numoftimes = int (input ('How many numbers do you want to input:'))

for x in range (numoftimes):
    x = int (input ('Please enter a whole number:'))
    y = int (input ('Please enter a greater whole number:'))
    nextnum = x
    total = 0
    if x < y:
        for nextnum in range (x, y + 1):
            total = total + nextnum
        print (total)
    else:
        print ('x must be less than y.')
