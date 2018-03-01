#Ruhika Chatterjee
#Pyhton Period 5
#October 19, 2015
#Calculate the permutation of two numbers.

n = int (input ('Please enter a value n:'))
r = int (input ('Please enter a value r:'))

NminusR = n - r

if n > r and r > 0:
    factorialN = 1
    for x in range (1, n + 1):
        factorialN = factorialN * x

    factorialNminusR = 1
    for y in range (1, NminusR + 1):
        factorialNminusR = factorialNminusR * y

    P = factorialN / factorialNminusR

    print ('The permutation of', n, 'and', r, 'is', P)
