#Ruhika Chatterjee
#Pyhton Period 5
#September 17, 2015
#Find the diameter, circumference, and area of a circle using the radius.

import math
pi = math.pi

def diameter (radius):
    diameter = radius * 2
    print ('The diameter is', diameter)

def circumference (radius):
    circumference = 2 * pi * radius
    print ('The circumference is', circumference)

def area (radius):
    area = pi * (radius ** 2)
    print ('The area is', area)

def main():
    r = int (input ('Please enter the radius of a circle:'))
    diameter (r)
    circumference(r)
    area(r)

main()
