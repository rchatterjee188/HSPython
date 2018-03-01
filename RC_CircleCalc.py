#Ruhika Chatterjee
#Pyhton Period 5
#September 17, 2015
#Find the diameter, circumference, and area of a circle using the radius.

#initialize pi
import math
pi = math.pi

#get the radius from user and convert into integer
radius = int(input('Please enter a radius:'))

#calculate and print diameter
diameter = radius * 2
print ('The diameter is', diameter)

#calculate and print circumference
circumference = 2 * pi * radius
print ('The circumference is', circumference)

#calculate and print area
area = pi * (radius ** 2)
print ('The area is', area)
