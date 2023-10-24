num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))

if num1 > num2:
    print(f'Numbers in ascending order: {num2, num1}')
    
elif num1 != num2:
    print(f'numbers in ascending order: {num1, num2}')
    
if num1 == num2:
    print(f'Numbers are equal: {num1, num2}')