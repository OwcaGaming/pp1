oldprice = int(input('Enter old price: '))
curprice = int(input('Enter current price: '))

discount = int(100-(curprice*100/oldprice))

if discount >= 10:

    print (f'The discount is {discount}%, you should buy!!!')
else:
    print('Ur gettin scammed')
   