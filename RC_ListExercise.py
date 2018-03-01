#Ruhika Chatterjee
#Python Period 5
#November 11, 2015
#Execise with lists

import random

even = 0
odd = 0

alist = []

for x in range (0,100):
    newnum = random.randint (10,500)
    addlist = [newnum]
    alist = alist + addlist


for y in range (10, 91, 10):
    print (alist [y], end = ' ')

print ()
print ()

for z in range(0,100):
    print (alist [z], end = ' ')

    if (alist [z] % 2) == 0:
        even = even + 1
    else:
        odd = odd + 1

print ()
print ()

print ('There are', even, 'even numbers, and', odd, 'odd numbers.')

