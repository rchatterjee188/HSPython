#Mrs. Guy
#Python 2015
#September 22, 2015
#yi_elseDoNow

import math

value1 = int(input("Please enter a value"))
value2 = int(input("Please enter another value"))

sqr_value1 = math.sqrt(value1)
sqr_value2 = math.sqrt(value2)

if sqr_value1 > sqr_value2:
    max_sqr = sqr_value1
else:
    max_sqr = sqr_value2

print("The larger square root is: ", max_sqr)
