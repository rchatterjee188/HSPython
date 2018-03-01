#Ruhika Chatterjee
#Python Period 5
#October 14, 2015
#Print 4 patterns of asterisks side-by-side

for x in range (10):
    for y in range (0, x + 1):
        print ('*', end = ' ')
    for y in range (x, 9):
        print (' ', end = ' ')
    print (' ', end = '')
    for y in range (x, 10):
        print ('*', end = ' ')
    for y in range (0, 2 * x):
        print (' ', end = ' ')
    print (' ', end = '')
    for z in range (x, 10):
        print ('*', end = ' ')
    for y in range (x, 9):
        print (' ', end = ' ')
    print (' ', end = '')
    for z in range (0, x + 1):
        print ('*', end = ' ')
    print ('')

#When the program is run, there are too many character.
#The screen must be stretched to see the patterns.
