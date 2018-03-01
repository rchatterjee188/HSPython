#Ruhika Chatterjee
#Python Period 5
#October 1, 2015
#Find out if a five digit number is a palindrome

#ask user for 5 digit string
isapal = int ( input ('Please enter a string of 5 numbers:'))

#single out the first and last digit
firstdigit = isapal // 10000
fifthdigit = isapal % 10

#single out the second and fourth digit
seconddigit = (isapal // 1000) % 10
fourthdigit = (isapal % 100) // 10

#calculate if first number equals last number and if second
#number equals fourth number. Print according message.
if firstdigit == fifthdigit and seconddigit == fourthdigit:
    print ('The string is a palindrome')
else:
    print ('The string is not a palindrome')
