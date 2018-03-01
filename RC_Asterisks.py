#Ruhika Chatterjee
#Python Period 5
#October 14, 2015
#Print 4 patterns of asterisks

for x in range (10):
    for y in range (0, x + 1):
        print ('*', end = ' ')
    print ('')

print ('')

for x in range (10):
    for y in range (x, 10):
        print ('*', end = ' ')
    print ('')

print ('')

for x in range (10):
    for y in range (0, x):
        print (' ', end = ' ')
    for z in range (x, 10):
        print ('*', end = ' ')
    print ('')

print ('')

for x in range (10):
    for y in range (x, 9):
        print (' ', end = ' ')
    for z in range (0, x + 1):
        print ('*', end = ' ')
    print ('')
