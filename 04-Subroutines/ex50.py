def factorial(n):
    fact = n
    if n == 1 or n == 0:
        return 1
    while n >= 2:
        fact *= (n-1)
        n -=1
    return fact    
print(factorial(4))