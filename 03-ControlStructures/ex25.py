num = int(input('Enter number of products: '))
price = int(input('Enter price of product: '))
total = 0

if num > 2:
    total = num*price*0.75
else:
    total = num*price
    
print(f'The total is: {total}')