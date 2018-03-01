#Ruhika Chatterjee
#Python Period 5
#October 19, 2015
#Print times table 10 x 10

for x in range (1, 11):
    for y in range (1, 11):
        if (x * y) >= 100:
            print (x * y, end = ' ')
        if (x * y) >= 10 and (x * y) < 100:
            print (x * y, end = '  ')
        if (x * y) < 10:
            print (x * y, end = '   ')
    print ('')
