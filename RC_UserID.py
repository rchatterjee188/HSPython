#Ruhika Chatterjee
#Python Period 5
#November 30, 2015
#Print a user id.

LASTNAMELEN = 7

def askuser ():
    firstname = input ('Please enter your first name:')
    firstname = firstname.lower()
    lastname = input ('Please enter your last name:')
    lastname = lastname.lower()
    return firstname, lastname

def main ():
    first, last = askuser ()

    if len (last) >= LASTNAMELEN:
        userid = last [:7] + first [0]

    else:
        userid = last + first [0]

    print ('Your user id is', userid)

main()
