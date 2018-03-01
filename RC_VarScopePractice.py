#Ruhika Chatterjee
#Python Period 5
#November 11, 2015
#Fixing syntax errors

def subtotal(inProd, inQuan):
    subT = 0
    if inProd == 1:
        subT = 2.3 * inQuan
    elif inProd == 2:
        subT = 4.5 * inQuan
    elif inProd == 3:
        subT = 1.2 * inQuan
    elif inProd == 4:
        subT = 8.9 * inQuan
    elif inProd == 5:
        subT = 2 * inQuan
    return subT

def main():
    total = 0
    yesNo = 'y'
    ###introduction()
    while yesNo == 'y':
        prd = int(input("What product would you like to order?"))
        quan = int(input("How many units of product "+ str(prd) + " would you like to order?"))
        subTotal = subtotal(prd, quan)
        total = total + subTotal
        yesNo = input("Do you want to add more products to your order?")
    
main()
