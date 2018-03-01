#Ruhika Chatterjee
#Pyhton Period 5
#September 17, 2015
#Find temperature based on cricket chirps

#get number of chirps from user, conver into integer,
#and convert from 'per 15 secs' to 'per 60 secs'
chirps = int(input('Please enter the number of cricket chirps in 15 seconds:'))
crirps = chirps * 4

#calculate and print temperature
temperature = (chirps / 4) + 40
print ('The temperature (in Fahrenheit) is', temperature)

#ask user if they want to play again
print ('Do you want to calculate the temperature again?')
response = input()

#check if user sais 'no'
answer = 0
if response == 'No' or response == 'no':
    answer = 1

#if user didn't say no, ask for # of chirps, calculate temp, and ask again
#if user doesn't say no again, repeat
while answer == 0:
    chirps = int(input('Please enter the number of cricket chirps in 15 seconds:'))
    crirps = chirps * 4
    
    temperature = (chirps / 4) + 40
    print ('The temperature (in Fahrenheit) is', temperature)
    
    print ('Do you want to calculate the temperature again?')
    response = input()

    if response == 'No' or response == 'no':
        answer = 1
