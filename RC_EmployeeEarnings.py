#Ruhika Chatterjee
#Python Perion 5
#January 20, 2016
#Give data on earinings of employee's

EMPLOYEEMONTHLYSALARY = [5000, 10000, 6500, 3600, 2500, 1200, 5100, 7100, 5900, 7000, 7800, 3600, 18000, 8400, 5000, 9000, 4500, 9000, 7500, 3900, 8000, 3400, 6900, 4800, 2100, 6600, 11000, 3700, 8900, 20000, 2700, 3140, 8300, 3900, 3600, 5600, 6000, 6200, 2300, 7800, 5100, 4600, 4000, 2900, 3000, 5900, 3700, 9400, 9900, 25000, 8800, 3600, 4200, 2400, 3300, 6000, 3700, 3000, 3200, 8500, 14000, 5200, 4700, 2500, 2900, 7800, 8300, 31000, 4300, 6200, 5400, 8300, 7400, 5200, 6500, 8200, 4400, 9400, 8300, 2100, 3600, 4100, 6700, 8100, 3200, 2800, 8700, 6200]

def calculateTotalEarnings ():
    totalEmployeeEarnings = []
    for i in range (len(EMPLOYEEMONTHLYSALARY)):
        totalEmployeeEarnings.append (int((EMPLOYEEMONTHLYSALARY[i] * 12) * 1.05))
    return totalEmployeeEarnings

def organizesSalaryRanges (totalEmployeeEarnings):
    frequency = [0] * 12
    for x in range (len(totalEmployeeEarnings)):
        if len(str(totalEmployeeEarnings[x])) < 5:
            frequency[0] += 1
        elif len(str(totalEmployeeEarnings[x])) > 5:
            if totalEmployeeEarnings[x] > 150000:
                frequency[-2] += 1
            else:
                frequency[-1] += 1
        else:
            index = int(str(totalEmployeeEarnings[x])[0])
            frequency[index] += 1
    return frequency

def printOutput (frequency):
    print ('The frequencies for the ranges are', frequency)
    for x in range (len(frequency)):
        if x != 0 and x != 10 and x != 11:
            range1 = '%6d' % (int(str(x) + '0000'))
            range2 = '%6d' % (int(str(x) + '9999'))
            print ('$' + range1[0:-3] + ',' + range1[-3:], '-', '$' + range2[0:-3] + ',' + range2[-3:], '* ' * frequency[x])
        elif x == 0:
            print ('$' + '%7d' % (0), '-', '$' + '%7d' % (999), '* ' * frequency[x])
        elif x == 10:
            print ('$' + '100,000 - $149,999', '* ' * frequency[x])
        else:
            print ('$' + '  150,000 and over', '* ' * frequency[x])

def main ():
    totalEmployeeEarnings = calculateTotalEarnings ()
    
    frequency = organizesSalaryRanges (totalEmployeeEarnings)
    
    printOutput (frequency)

main ()
