#Ruhika Chatterjee
#Python Period 5
#September 29, 2015
#Determine if the angles make a right triangle run again if user wishes

#initialize variable for loop
yesno = 'y'

#ask user for 3 #s. Check if they make a triangle, check if it makes a
#right triangle, print message accordingly. Ask if user wants to play aqain.
while yesno == 'y':
    angle1 = float ( input ('Please enter an angle:'))
    angle2 = float ( input ('Please enter another angle:'))
    angle3 = float ( input ('Please enter a third angle:'))
    
    checktriangle = angle1 + angle2 + angle3
    
    if checktriangle == 180:
        if angle1 == 90 or angle2 == 90 or angle3 == 90:
            print ('This is a right triangle.')
        else:
            print ('This is not a right triangle.')
    else:
        print ('The angles do not equal a triangle.')
    
    yesno = input ('Do you want to play again? (y/n):')

