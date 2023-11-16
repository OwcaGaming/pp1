'''
(p1.py) The vending machine accepts
1, 2 and 5 PLN coins. Define the function
f(amount_to_pay) that returns the minimum number
of coins that can be used to pay
for the purchased product.
'''
def f(n):
 coins = 0
 while n >= 0:
     if n >= 5:
         n -= 5
         coins += 1
     else:
         break
 while n >= 0:
     if n >= 2:
         n -= 2
         coins += 1
     else:
         break
 while n >=0:
     if n >= 1:
         n -= 1
         coins += 1
     else:
         break
 return coins

if __name__ == '__main__':
    #check your program in this place
    print(f(31))
    print(f(8))
    print(f(2))
    print(f(0))
