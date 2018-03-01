#Ruhika Chatterjee
#Pyhton Period 5
#October 6, 2015
#Tell the user the intensity of the earthquake based on the richter scale.

yesNo = 'y'

while yesNo == 'y':
    richter = float ( input ('Please enter the magnitude of the earthquake (richter scale):'))
    
    if richter < 0:
        print ('This is an invalid input')
    elif richter <= 1.9:
        print ('This is a micro earthquake')
    elif richter <= 3.9:
        print ('This is a minor earthquake')
    elif richter <= 4.9:
        print ('This is a light earthquake')
    elif richter <= 5.9:
        print ('This is a moderate earthquake')
    elif richter <= 6.9:
        print ('This is a strong earthquake')
    elif richter <= 7.9:
        print ('This is a major earthquake')
    elif richter <= 9.9:
        print ('This is a great earthquake')
    elif richter >= 10:
        print ('This is an epic earthquake')

    yesNo = input ('Do you want to run it again? (y/n):')
