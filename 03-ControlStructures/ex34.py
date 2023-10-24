num = int(input('Enter price: '))
five = 0
two = 0
one = 0

while num >= 5:
    num -= 5
    five += 1
    
while num >= 2:
    num -= 2
    two += 1

while num >= 1:
    num -= 1
    one += 1
    
print(f'Amount of 5zl coins: {five}, amount of 2zl coins: {two}, amount of 1zl coins: {one}')