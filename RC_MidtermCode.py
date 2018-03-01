#Ruhika Chatterjee
#Python Period 5
#February 1, 2016
#Calculate ranges of broker fees.

INVESTMENTS_LIST = [4850, 4360, 5180, 3690, 640, 2560, 5150, 7120, 5920, 7080, 7830, 3600, 1820, 8460, 566, 547, 134, 6600, 7810, 3950, 8010, 325, 690, 634, 2100, 6670, 8950, 3730, 1890, 6240, 2170, 670, 8500, 314, 8000, 333, 8670, 326, 6560, 7760, 620, 203, 7300, 5510, 4360, 7040, 5100, 7820, 4820, 5690, 7750, 1870, 2990, 2660, 8860, 7010, 3640, 3700, 1410, 2400, 1750, 4600, 3270, 2890, 2430, 3240, 8050, 3000, 5200, 7300, 1680, 7200, 7620, 2960, 7830, 8730, 3100, 4330, 1960, 5740, 8930, 7240, 5200, 6530, 7100, 4440, 4240, 3890, 2320, 3760, 4110, 5760, 8190, 4100, 2860, 8760, 6260, 7420]
RANGES = ['$100 - $199', '$200 - $299', '$300 - $399', '$400 - $499', '$500 - $599', '$600 - $699', '$700 - $799', '$800 - $899', '$900 - $999', '$1000 and up']

def calcBrokerFee ():
    #Convert investments to broker's fees by appending to new list
    brokerFee = []
    for i in range (len(INVESTMENTS_LIST)):
        brokerFee.append(int(INVESTMENTS_LIST[i] * 0.09 + 100))
    return brokerFee

def getFrequency (brokerFee):
    #Calculate the frequency of the ranges and add to the frequency list
    frequency = [0] * 10
    for i in range (len(brokerFee)):
        if len(str(brokerFee[i])) >= 4:
            frequency [-1] += 1
        else:
            frequency[int(str(brokerFee[i])[0])-1] += 1

    return frequency

def printHistogram (freq):
    #Print results using a histogram
    for i in range (len(freq)):
        print ('%12s' % (RANGES[i]), '%2d' % (freq[i]), '*' * freq[i])

def main ():
    brokerFee = calcBrokerFee ()
    frequency = getFrequency (brokerFee)
    
    printHistogram (frequency)

main ()
    
