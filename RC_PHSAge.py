#Ruhika Chatterjee
#Python Period 5
#September 21, 2015
#Ask the user for the age of PHS

age = 116
answer = 0

answer = int(input("How old is PHS?"))

while answer != age:
    print ("Incorrect. Try again")
    answer = int(input("How old is PHS?"))

print ("Correct")

