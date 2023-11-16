
def numbers(n):
    n = tuple(str(n))
    num = str('')
    for i in range(len(n)):
        num += n[i] + ' '
    
    
a = int(input('Enter number: '))
print(numbers(a))
