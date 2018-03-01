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

def getFrequency (data, frequency):
    for i in range(len(data)):
        frequency[data[i]-1] += 1
    return frequency

def main ():
    dataList = []
    dataList = getRandomList (dataList)

    frequency = [0] * 10
    frequency = getFrequency (dataList, frequency)

    print (frequency)

main()
