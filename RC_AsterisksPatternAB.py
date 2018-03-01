#Ruhika Chatterjee
#Python Period 5
#October 15, 2015
#Print 2 patterns of asterisks

for x in range (10):
    for y in range (0, x + 1):
        print ('*', end = ' ')
    print ('')

print ('')

for x in range (10):
    for y in range (x, 10):
        print ('*', end = ' ')
    print ('')
