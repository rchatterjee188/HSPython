#Ruhika Chatterjee
#Python Period 5
#September 23, 2015
#Find the range of an unlimited number of numbers

number = []
isTrue = False
counter = 3

#Gets from user and adds first number to list
num = float (input ('Please enter value' + str(1) + ':'))
number.append (num)

#Gets from user and adds second number to list to the end or beggining
#based on if it is greater or less than the first number
num = float (input ('Please enter value' + str(2) + ':'))
if num > number[0] or num == number[0]:
    number.append(num)
else:
    number.insert(0, num)

#Gets other numbers from user and replaces the higher number if it
#is greater than that number and replaces the lower number if it is
#lower that that number. Goes on to next step if user presses enter.
while isTrue == False:
    num = input ('Please enter value' + str(counter) + '(Press enter if you have no more numbers):')
    if num != '':
        num = float (num)
        if num < number[0]:
            number[0] = num
        elif num > number[1]:
            number[1] = num
    else:
        isTrue = True
    counter = counter + 1

least = number [0]
greatest = number [1]

calcrange = greatest - least

print ('The range is', calcrange)
