#Ruhika Chatterjee
#Pyhton Period 5
#October 19, 2015
#Calculate the combination of two numbers.

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

    factorialR = 1
    for z in range (1, r + 1):
        factorialR = factorialR * z

    P = factorialN / (factorialR * factorialNminusR)

    print ('The permutation of', n, 'and', r, 'is', P)

else:
    print ('Those are not valid inputs')
