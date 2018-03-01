#Ruhika Chatterjee
#Python Period 5
#February 8, 2015
#Have dictionaries of grades and find averages.
#Assumption: There is only one student with the highest average.

def getGrades (tests):
    whoinput = 0
    while whoinput != 1 and whoinput != 2:
        whoinput = int (input ('Do you want to input the data yourself (1) or have the computer enter data (2)?:'))
        
    if whoinput == 1:
        for i in range (5):
            student = input ('Please enter the name of the student:')
            grade1 = int (input ('Please enter his/her grade on the first test:'))
            grade2 = int (input ('Please enter his/her grade on the second test:'))
            grade3 = int (input ('Please enter his/her grade on the third test:'))
            print ()
            tests[0].update ({student:grade1})
            tests[1].update ({student:grade2})
            tests[2].update ({student:grade3})
    elif whoinput == 2:
        tests [0].update ({'Joe':88, 'Christina':99, 'Simon':76, 'Emily':92, 'Elizabeth':78})
        tests [1].update ({'Joe':98, 'Christina':87, 'Simon':90, 'Emily':96, 'Elizabeth':100})
        tests [2].update ({'Joe':92, 'Christina':96, 'Simon':89, 'Emily':94, 'Elizabeth':93})
        
    return tests[0],tests[1],tests[2]

def getAverages (tests):
    keys = tests[0].keys ()
    averages = {}
    
    for student in keys:
        averages.update({student:(tests[0][student] + tests[1][student] + tests[2][student])/3})
    
    return averages

def getHighestAverage (averages):
    students = list(averages.keys())
    highest = students[0]
    for student in students:
        if averages[student] > averages[highest]:
            highest = student
    return highest

def printAverages (highest, averages):
    students = averages.keys()
    print ("The student's grade averages are:")
    for student in students:
        print (student + ':', int(averages[student]))
    print ('The sudent with the highest average is', highest)

def main ():
    test1 = {'bob':88, 'lisa':100}
    test2 = {'bob':85, 'lisa':95}
    test3 = {'bob':80, 'lisa':98}

    test1, test2, test3 = getGrades ([test1, test2, test3])

    averages = getAverages ([test1, test2, test3])

    highest = getHighestAverage (averages)

    printAverages (highest, averages)

main ()
