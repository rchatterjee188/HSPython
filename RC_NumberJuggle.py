#Ruhika Chatterjee
#Python Period 5
#September 28, 2015
#Do random operations to birth year and age and repeat if user wishes

yesNo = 'y'

while yesNo == 'y':
    year = int ( input ( 'Please enter your birth year:'))
    age = int ( input ( 'Please enter your age:'))
    
    juggle = float ((((((year * 2) + 5) * 50) + age) - 250) / 100)
    
    print ("%.2f" % juggle)

    yesNo = str ( input ('Do you want to play again?(y/n):'))
