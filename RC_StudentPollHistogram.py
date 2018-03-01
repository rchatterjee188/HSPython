#Ruhika Chatterjee
#Python Period 5
#January 13, 2016
#Organize a poll

import random

NUMSTUDENTS = 16

def getRandomList (dataList):
    for x in range (NUMSTUDENTS):
        dataList.append (random.randint (1,10))
    return dataList

def getFrequency (dataList, frequency):
    for x in range (len (dataList)):
        frequency[dataList[x]] += 1
    return frequency

def printHistogram (frequency):
    for x in range (1, len(frequency)):
        print ('%2d' % (x), '* ' * frequency[x]) 

def main ():
    dataList = []
    dataList = getRandomList (dataList)

    frequency = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    frequency = getFrequency (dataList, frequency)

    print ('The data is:', dataList)
    print ('The frequency is:', frequency)

    printHistogram (frequency)

main ()
