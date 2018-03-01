#Ruhika Chatterjee
#Python Period 5
#October 2, 2015
#Calculates the mortgage

borrowed = float ( input ('Enter how much being borrowed:')) #total amount borrowed
years = int ( input ('Enter the number of years:')) #number of years
rate = float ( input ('Enter the annual rate (%):')) #rate per year
rate = rate / 1200 #rate per month in decimal form
months = years * 12 #number of months

numerator = rate * borrowed
denominator = 1 - ((1 + rate) ** (-1 * months))

monthly = round (numerator / denominator)

total = round (monthly * 12 * years)

print ('The monthly payment is', monthly)
print ('the total amount you pay is', total)

