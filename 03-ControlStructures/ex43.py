num1 = 0
num2 = 1

for i in range(0, 20):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
    print(f'{num3}', end=' ')
