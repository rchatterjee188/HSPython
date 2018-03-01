#Ruhika Chatterjee
#Python Period 5
#January 18, 2016
#Print histogram of exam scores.

import random

NUMOFSTUDENTS = 25
GRADES = ['A Range', 'B Range', 'C Range', 'D Range', 'F Range']

def getGrades ():
    studentGrades = []
    for x in range (NUMOFSTUDENTS):
        studentGrades.append (random.randint(0,100))
    return studentGrades

def organizeGrades(studentGrades):
    examScores = [0, 0, 0, 0, 0]
    for i in range (NUMOFSTUDENTS):
        if studentGrades[i] >= 90:
            examScores[0] += 1
        elif studentGrades[i] >= 80:
            examScores[1] += 1
        elif studentGrades[i] >= 70:
            examScores[2] += 1
        elif studentGrades[i] >= 60:
            examScores[3] += 1
        else:
            examScores[4] += 1
    return examScores

def printOutput (studentGrades, examScores):
    print ('The students grades were', studentGrades)
    print ('The results by letter grade were', examScores)
    print ()
    for x in range (len(examScores)):
        print (GRADES[x], '*' * examScores[x])

def printPassFail (examScores):
    print (examScores[4] + examScores[3], 'students failed the midterms.')
    print (examScores[0] + examScores[1] + examScores[2], 'students passes the midterms.')

def main ():
    studentGrades = getGrades ()
    examScores = organizeGrades (studentGrades)
    
    printOutput (studentGrades, examScores)
    print ()
    printPassFail (examScores)


main()
