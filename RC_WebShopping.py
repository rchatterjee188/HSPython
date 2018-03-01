#Ruhika Chatterjee
#Python Period 5
#October 22, 2015
#Calculate the total price of 5 items bought online on a website.

def listofproducts (num, product, price,description):
    print ('Product #' + num + ':', product + ':', price + '-', description)
    
def printproducts ():
    print ('Welcome to A Sirius Obsession! These are a list of our most popular products:')
    print ('')
    listofproducts('1', 'A Wand', '10 galleons', 'A fur wood with a dragon heartstring.')
    listofproducts('2', "Berty Bott's Jelly Beans", '3 sickles', "Never know what's next!")
    listofproducts('3', 'An Owl', '50 galleons', 'A grey owl trained in delivery for 3 years.')
    listofproducts('4', 'A Quill', '2 sickles', 'A self-inking quill')
    listofproducts('5', 'A Chocolate Frog', '5 sickles', "They'll hop away! Collect your cards.")
    print ('')

def calculategalleons (prodnum,howmany,galleons):
    if prodnum == 1:
        cost = 10
    elif prodnum == 3:
        cost = 50
    
    galleons = galleons + (cost * howmany)

    return galleons
    

def calculatesickles (prodnum,howmany,sickles):
    if prodnum == 2:
        cost = 3
    elif prodnum == 4:
        cost = 2
    elif prodnum == 5:
        cost = 5

    sickles = sickles + (cost * howmany)

    return sickles

def printadded (prodnum,howmany):
    if prodnum == 1:
        prod = 'Wand'
    elif prodnum == 2:
        prod = "Berty Bott's Jelly Beans"
    elif prodnum == 3:
        prod = 'Owl'
    elif prodnum == 4:
        prod = 'Quill'
    elif prodnum == 5:
        prod = 'Chocolate Frog'
        
    if howmany == 1:
        print (howmany, 'unit of', prod, 'has been added to your shopping cart.')
    elif prod == "Berty Bott's Jelly Beans":
        print (howmany, 'units of', prod, 'have been added to your shopping cart.')
    else:
        print (howmany, 'units of', prod + 's have been added to your shopping cart.')


def main():
    galleons = 0
    sickles = 0
    yesNo = 'yes'
    
    printproducts()

    while yesNo == 'yes' or yesNo == 'Yes':
        productnum = int (input ('Product number:'))
        quantity = int (input ('Quantity:'))

        if productnum == 1 or productnum == 3:
            galleons = calculategalleons (productnum,quantity,galleons)
            printadded (productnum,quantity)
        elif productnum == 2 or productnum == 4 or productnum == 5:
            sickles = calculatesickles (productnum,quantity,sickles)
            printadded (productnum,quantity)
        else:
            print ('That is not a valid product number.')
            
        yesNo = input ('Do you want to play again or print the products again? (yes/no/products):')

        if yesNo == 'Products' or yesNo == 'products':
            printproducts()
            yesNo = 'yes'
            
        print ('')

    if sickles >= 17:
        galleons = galleons + (sickles // 17)
        sickles = sickles % 17

    address = input ('What address would you like the products to be shipped to?')
    
    print ('')
    print ('The total price is', galleons, 'galleons and', sickles, 'sickles.')
    print ('Your products will be shipped to', address)


main()

