#Ruhika Chatterjee
#Python Period 5
#October 21, 2015
#Convert fahrenheit to celsius or celsius to fahrenheit.

yesNo = 'yes'

while yesNo == 'yes' or yesNo == 'Yes':
    def fartocel (temperature):
        celcius = (temperature - 32.0) * (5/9)
        return celcius

    def celtofar (temperature):
        farenheit = (temperature * 1.8) + 32.0
        return farenheit

    def main ():
        typeoftemp = input ('Do you want to enter a temperature in fahrenheit or celsius?:')

        if typeoftemp == 'celsius' or typeoftemp == 'Celsius':
            temp = float (input ('Please enter a temperture:'))
            finaltemp = celtofar (temp)

        if typeoftemp == 'farenheit' or typeoftemp == 'Farenheit':
            temp = float (input ('Please enter a temperture:'))
            finaltemp = fartocel (temp)

        print ('The temperature is',  finaltemp)

    main()

    yesNo = input ('Do you want to play again? (yes/no):')
