#Ruhika Chatterjee
#Python Period 5
#October 8, 2015
#Add the numbers between and including x and y.

yesNo = 'y'

while yesNo == 'y' or yesNo == 'Y' or yesNo == 'yes' or yesNo == 'Yes':
    x = int (input ('Please enter a whole number:'))
    y = int (input ('Please enter a greater whole number:'))
    
    nextnum = x
    total = 0
    
    if x < y:
        while nextnum <= y:
            total = total + nextnum
            nextnum = nextnum + 1

        print (total)
        
    else:
        print ('x must be less than y')

    yesNo = input ('Do you want to pay again? (y/n):')
