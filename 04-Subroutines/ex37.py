def fibonacci(n):
    num1 = 0
    num2 = 1
    num3 = 0
    i=1
    if n == 1:
        return num1
    if n == 2:
        return num2
    if n == 3:
        return num2
    while i < n-1:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        i += 1
    return num3


print(fibonacci(7))