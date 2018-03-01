#Ruhika Chatterjee
#Python Period 5
#December 6, 2015
#Create a "data base" for students names
#Assumption: User does not enter a letter for options or classes.

OPTIONNUMBERS = [1, 2, 3, 4]
CLASSNUMBERS = [1, 2, 3, 4, 5]

def printInputs ():
    #Prints all the possible inputs for the options
    print ('Option 1: Add a student to a class')
    print ('Option 2: Delete a student from a class')
    print ('Option 2: Print all the students from a class')
    print ('Option 2: Print all the students from all  the classes')
    print ()
    
def getInput ():
    #Gets an input and data validates till user enters a valid input
    while True:
        inp = int (input ('Please choose one of the options (1-4):'))
        if inp in OPTIONNUMBERS:
            return inp

def getClass (type1):
    #Asks user for a class (data validation)
    while True:
        if type1 == 'add':
            aclass = int (input ('Which class would you like to add a name to (1-5)?:'))
        elif type1 == 'del':
            aclass = int (input ('Which class would you like to remove a name from (1-5)?:'))
        elif type1 == 'print':
            aclass = int (input ('Which class would you like to print the names from (1-5)?:'))
        
        if aclass in CLASSNUMBERS:
            return aclass
        else:
            print ('That is not a valid class number')
    
def getName (type1,classes,classindex):
    #Asks for name (data validation)
    while True:
        if type1 == 'add':
            name = input ('What is the name of the student you would like to add?:')
            if name not in classes[classindex]:
                return name
            else:
                print ('That name is already in that class')
        elif type1 == 'del':
            name = input ('What is the name of the student you would like to remove?:')
            if name in classes[classindex]:
                return name
            else:
                print ('That name is not in that class')

def addStudent (classes):
    #Append name to correct list and print that name was added, and return new classes list
    aclass = getClass ('add')
    classindex = aclass - 1
    name = getName ('add',classes,classindex)
    classes[classindex].append (name)
    print (name, 'was added to class', aclass)
    print ()
    return classes
        
            

def deleteStudent (classes):
    #Remove name from correct list and print that name was removed, and return new classes list
    aclass = getClass ('del')
    classindex = aclass - 1
    if not not classes [classindex]:
        name = getName ('del',classes,classindex)
        classes[classindex].remove (name)
        print (name, 'was removed from class', aclass)
        print ()
    else:
        print ('That class has no students')
    return classes


def printAClass (classes):
    #Asks user for a class (data validation), uses for loop to print all the names
    aclass = getClass ('print')
    classindex = aclass - 1
    if not not classes [classindex]:
        for name in classes [classindex]:
            print (name)
        print ()
    else:
        print ('That class has no students')

def printAllClasses (classes):
    #Uses nested for loop to print all the names undeer each class
    for i in range(len(classes)):
        print ('Students in class', str(i+1) + ':')
        for name in classes[i]:
            print (name)
    print ()

def playAgain ():
    #Asks user if they want to play again and return a boolean
    again = input ('Do you want to execute another action? (yes/no):')
    return again.lower().startswith ('y')
    
def main ():
    #Defines list of lists for classes
    classes = [ [], [], [], [], [] ]
    #Welcome message
    print ('Welcome to The Student Tracker')
    print ('What do you want to do?')
    print ()

    #To run till user doesn't want to play anymore
    while True:
        #Prints options and get input
        printInputs()
        inp = getInput ()

        #Calls function based on input of options
        if inp == 1:
            classes = addStudent (classes)
        if inp == 2:
            classes = deleteStudent (classes)
        if inp == 3:
            printAClass (classes)
        if inp == 4:
            printAllClasses (classes)

        #Asks user if they want to play again
        again = playAgain ()
        if not again:
            #If not again, print goodbye message and end loop and game
            print ('Thanks for using Student Tracker. Goodbye!')
            break

main ()
