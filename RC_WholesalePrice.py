#Ruhika Chatterjee
#Pyhton Period 5
#September 16, 2015
#Find the price of book based on # of copies ordered

#calculate the price of books with the discount
bookprice = 24.95 * 0.6

#get number of copies from user and convert into integer
numofbook = int(input('Please enter the number of copies:'))

#calculate and print total price of the books
total = (bookprice * numofbook) + 3 + (0.75 * (numofbook - 1))
print ('The cost of', numofbook, 'books is $' + str(total)) 
